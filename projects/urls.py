from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="list"),
    path("detail/<str:slug>/", views.ProjectDetailView.as_view(), name="detail"),
]
