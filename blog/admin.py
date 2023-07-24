from django.contrib import admin
from . import models
from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        FroalaField: {"widget": FroalaEditor},
    }
