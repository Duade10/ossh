from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db.models import TextField

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {"widget": TinyMCE()},
    }
