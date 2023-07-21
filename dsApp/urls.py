from .views import dswelcome
from django.urls import path

urlpatterns = [
    path("", dswelcome),
]