from django.urls import path, include
from rest_framework import routers
from .views import *
from .viewsSet import *


router = routers.DefaultRouter()
router.register(r"dogs", DogViewSet)
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("api/", include(router.urls)),
    path("create-dog", CreateDogView.as_view(), name="create-dog"),
]

router.register(r"dogs", DogViewSet, basename="dogs")

urlpatterns += router.urls
