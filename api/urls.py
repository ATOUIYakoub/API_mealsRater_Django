from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewsets, RatingViewsets

router = routers.DefaultRouter()
router.register('meals',MealViewsets)
router.register('ratings',RatingViewsets)

urlpatterns = [
    path('',include(router.urls))
]
