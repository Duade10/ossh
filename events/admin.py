from django.contrib import admin
from . import models
from django.db.models import TextField
from tinymce.widgets import TinyMCE


class EventImageInline(admin.TabularInline):
    model = models.EventImage


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "location", "start_time", "end_time", "is_active"]
    inlines = [
        EventImageInline,
    ]
    formfield_overrides = {
        TextField: {"widget": TinyMCE()},
    }


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
