from django.shortcuts import render, get_object_or_404
from django.views import View
from . import models


class ProjectListView(View):
    def get(self, request, *args, **kwargs):
        projects = models.Project.objects.all()
        return render(request, "projects/projects.html", {"projects": projects})


class ProjectDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            project = get_object_or_404(models.Project, slug=slug)
        except models.Project.DoesNotExist:
            pass
        return render(request, "projects/project_detail.html", {"project": project})
