from django.contrib import admin
from . import models
from django.db.models import TextField
from tinymce.widgets import TinyMCE


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {"widget": TinyMCE()},
    }
