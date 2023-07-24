from django.contrib import admin
from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        FroalaField: {"widget": FroalaEditor},
    }
