from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("", views.EventsListView.as_view(), name="list"),
    path("ticket/<str:event_id>/<str:email>/", views.Ticket.as_view(), name="ticket"),
    path("detail/<int:pk>/", views.EventDetailView.as_view(), name="detail"),
    path("confirm/<uidb64>/<eid>/", views.ConfirmRegistrationEmail.as_view(), name="confirm"),
    path("register/<str:slug>/", views.RegistrationView.as_view(), name="registration"),
    path("send-confirmation-message/<str:email>/", views.SendRegistrationEmail.as_view(), name="send_confirm"),
]
