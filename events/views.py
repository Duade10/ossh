import socket

from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode
from django.views.generic import DetailView, ListView, View
from django.http import JsonResponse

from . import forms, models


class EventsListView(ListView):
    model = models.Event
    template_name = "events/list.html"
    context_object_name = "events"


class EventDetailView(DetailView):
    model = models.Event
    template_name = "events/detail.html"
    context_object_name = "event"


class RegistrationException(BaseException):
    pass


class RegistrationView(View):
    def get(self, request, slug, *args, **kwargs):
        event = models.Event.objects.get(slug=slug)
        form = forms.RegistrationForm(initial={"event": event.pk})
        context = {"form": form, "event": event}
        return render(request, "events/registration.html", context)

    def post(self, request, slug, *args, **kwargs):
        url = request.META.get("HTTP_REFERER")
        event = models.Event.objects.get(slug=slug)
        form = forms.RegistrationForm(request.POST, initial={"event": event.pk})
        if form.is_valid():
            data = form.save(commit=False)
            data.event = event
            if models.Registration.objects.filter(email_address=data.email_address, event=event).exists():
                messages.info(request, "Email Already Registered")
                return redirect(url)
            data.save()
            reg = models.Registration.objects.get(id=data.id)
            try:
                reg.send_confirmation_mail(request)
                messages.warning(request, "Confirmation Email has been sent to your mail")
                return redirect("events:list")
            except socket.gaierror:
                pass
        context = {"form": form, "event": event}
        return render(request, "events/registration.html", context)


class SendRegistrationEmail(View):
    def get(self, request, email, *args, **kwargs):
        reg = models.Registration.objects.get(email_address=email)
        try:
            reg.send_confirmation_mail(request)
            messages.warning(request, "Confirmation message sent")
        except socket.gaierror:
            pass
        return redirect("events:list")


class ConfirmRegistrationEmail(View):
    def get(self, request, uidb64, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            registered = models.Registration.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, models.Registration.DoesNotExist):
            registered = None

        if registered is not None:
            registered.generate_qr_code()
            if not registered.is_email_confirm:
                messages.warning(request, "Email Verification Activation Successfull")
            registered.is_email_confirm = True
            registered.save()
        return redirect(
            f"/events/register/{registered.event.slug}?command=verification&email={registered.email_address}"
        )


class Ticket(View):
    def get(self, request, email, *args, **kwargs):
        reg = models.Registration.objects.get(email_address=email)
        return render(request, "events/ticket.html", {"reg": reg})
