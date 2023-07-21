from .views import fswelcome
from django.urls import path

urlpatterns = [
    path("", fswelcome),
]