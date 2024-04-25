from django.urls import path
from . import views

urlpatterns = [
    path("", views.signins, name="Sign-ins"),
    path("signin/", views.signins, name="Sign-ins"),
    path("processsignin/", views.processsignin, name="Process Sign In"),
    path("complete/", views.complete, name="Sign In Complete")
]
