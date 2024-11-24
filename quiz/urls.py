from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="list"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.CreateView.as_view(), name="create"),
]
