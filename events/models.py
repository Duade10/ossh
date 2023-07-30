from io import BytesIO

import qrcode
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.files import File
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from django.utils.text import slugify
from PIL import Image, ImageDraw

from core.models import AbstractTimestampModel


class Event(AbstractTimestampModel):
    image = models.ImageField(upload_to="event/main/")
    title = models.CharField(max_length=2500)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=2500, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class EventImage(AbstractTimestampModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="events/sub/")

    def __str__(self):
        return self.event.title


class Registration(AbstractTimestampModel):
    PARTICIPANT_TYPE = (("teams", "Teams"), ("individial", "Individual"))

    event = models.ForeignKey(Event, related_name="events", on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=500)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    organization = models.CharField(max_length=1500, blank=True, null=True)
    participant_type = models.CharField(max_length=15, choices=PARTICIPANT_TYPE, blank=True, null=True)
    number_of_participants = models.IntegerField(blank=True, null=True)
    is_email_confirm = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to="events/qr_codes", blank=True, null=True)

    def __str__(self):
        return f"{self.event.title} | {self.full_name}"

    def get_ticket_url(self):
        return reverse("events:ticket", kwargs={"email": self.email_address})

    def generate_qr_code(self):
        print("QRCODE")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"{self.full_name} | {self.event.title}")
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        canvas = Image.new("RGB", (400, 400), "white")
        ImageDraw.Draw(canvas)
        canvas.paste(img)
        file_name = f"QR_CODE{self.full_name}.png"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(file_name, File(buffer), save=True)
        canvas.close()
        self.save()

    def send_confirmation_mail(self, request):
        current_site = get_current_site(request)
        domain = current_site
        uid = urlsafe_base64_encode(force_bytes(self.pk))
        eid = urlsafe_base64_encode(force_bytes(self.event.pk))

        html_message = render_to_string(
            "events/mail/sign_up_email_confirmation.html",
            {"domain": domain, "uidb64": uid, "eid": eid, "full_name": self.full_name},
        )
        send_mail(
            "Activate your Account",
            strip_tags(html_message),
            settings.EMAIL_HOST_USER,
            [self.email_address],
            fail_silently=True,
            html_message=html_message,
        )
        self.save()
