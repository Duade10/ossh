from django.contrib import admin
from . import models


class EventImageInline(admin.TabularInline):
    model = models.EventImage


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventImageInline,
    ]


@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "email_address",
        "is_email_confirm",
        "participant_type",
        "number_of_participants",
        "event",
    ]
