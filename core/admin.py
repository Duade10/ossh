from django.contrib import admin
from froala_editor.fields import FroalaField
from froala_editor.widgets import FroalaEditor

from . import models


class IndexImageInline(admin.TabularInline):
    model = models.IndexCarouselImage
    extra = 0
    max_num = 3


@admin.register(models.IndexData)
class IndexDataAdmin(admin.ModelAdmin):
    inlines = [IndexImageInline]

    def has_add_permission(self, request) -> bool:
        return False


@admin.register(models.AboutData)
class AdminDataAdmin(admin.ModelAdmin):
    formfield_overrides = {
        FroalaField: {"widget": FroalaEditor},
    }

    def has_add_permission(self, request) -> bool:
        return False


@admin.register(models.FoundryDataContent)
class FoundryDataAdmin(admin.ModelAdmin):
    formfield_overrides = {
        FroalaField: {"widget": FroalaEditor},
    }

    def has_add_permission(self, request) -> bool:
        return False
