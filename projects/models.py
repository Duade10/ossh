from django.db import models
from core.models import AbstractTimestampModel
from django.utils.text import slugify
from django.urls import reverse


class ProjectPageBanner(AbstractTimestampModel):
    image = models.ImageField(upload_to="projects/banner/", blank=True, null=True)

    def __str__(self):
        return "Project Page Banner"


class Project(AbstractTimestampModel):
    image = models.ImageField(upload_to="projects/")
    title = models.CharField(max_length=3500)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
