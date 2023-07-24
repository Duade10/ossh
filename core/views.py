from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound

from . import models


class IndexView(View):
    def get(self, request, *args, **kwargs):
        page_data = models.IndexData.objects.last()
        carousel_images = page_data.indexcarouselimage_set.all()
        return render(request, "core/index.html", {"page_data": page_data, "carousel_images": carousel_images})


class AboutView(View):
    def get(self, request, *args, **kwargs):
        page_data = models.AboutData.objects.last()
        return render(request, "core/about.html", {"page_data": page_data})


class FoundryView(View):
    def get(self, request, *args, **kwargs):
        page_data = models.FoundryDataContent.objects.last()
        return render(request, "core/startup_foundry.html", {"page_data": page_data})
