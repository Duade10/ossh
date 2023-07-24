from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("detail/<int:pk>", views.PostDetailView.as_view(), name="detail"),
]
