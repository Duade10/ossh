from django.db import models
from django.urls import reverse

from core.models import AbstractTimestampModel


class BlogPageBanner(AbstractTimestampModel):
    image = models.ImageField(upload_to="blog/banner/", blank=True, null=True)

    def __str__(self):
        return "Blog Page Banner"


class Post(AbstractTimestampModel):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=2500)
    content = models.TextField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})
