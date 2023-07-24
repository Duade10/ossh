from django.db import models
from django.utils.translation import gettext_lazy as _
from froala_editor.fields import FroalaField


class AbstractTimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IndexData(AbstractTimestampModel):
    # Hero Section
    hero_text = models.CharField(_("Hero Section Text"), max_length=2500)
    hero_image = models.ImageField(_("Hero Section Image"), upload_to="index/hero")

    # Team Section
    team_text = models.CharField(_("Team Section Text"), max_length=2500)
    team_image = models.ImageField(_("Team Section Image"), upload_to="index/team", blank=True, null=True)

    # Section 3
    section_3_text = models.CharField(_("Section 3 Text"), max_length=2500)
    section_3_image = models.ImageField(_("Section 3 Image"), upload_to="index/section_3")

    class Meta:
        verbose_name = "Index Page Content"
        verbose_name_plural = "Index Page Content"

    def __str__(self):
        return "Index Page Texts and Image"


class IndexCarouselImage(AbstractTimestampModel):
    index = models.ForeignKey(IndexData, on_delete=models.CASCADE, default=1)
    text = models.CharField(max_length=50, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    file = models.ImageField(upload_to="index/carousel")

    def __str__(self):
        return f"Image {self.id}"


class AboutData(AbstractTimestampModel):
    banner = models.ImageField(_("About Us Page Banner"), upload_to="about/", blank=True, null=True)
    main_text = FroalaField(_("Main Text"))
    vision = models.TextField(_("OSSH Vision"))
    mission = models.TextField(_("OSSH Mission"))
    objective = models.TextField(_("OSSH Objective"))

    class Meta:
        verbose_name = "About Us Page Content"
        verbose_name_plural = "About Us Page Content"

    def __str__(self):
        return "About Us Page Texts"


class FoundryDataContent(AbstractTimestampModel):
    banner = models.ImageField(_("Startup Foundry Page Banner"), upload_to="foundry/", blank=True, null=True)
    content = FroalaField()

    class Meta:
        verbose_name = "Foundry Page Content"
        verbose_name_plural = "Foundry Page Content"

    def __str__(self):
        return "Startup Foundry Data Content"
