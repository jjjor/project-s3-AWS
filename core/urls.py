from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsSet import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
