from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db.models import TextField

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
        TextField: {"widget": TinyMCE()},
    }

    def has_add_permission(self, request) -> bool:
        return False


@admin.register(models.FoundryDataContent)
class FoundryDataAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {"widget": TinyMCE()},
    }

    def has_add_permission(self, request) -> bool:
        return False


@admin.register(models.TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "skill", "role")
