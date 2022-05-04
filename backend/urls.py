from posixpath import basename
from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('providers', views.ProviderViewSet, basename='providers')
router.register('service-areas', views.ServiceAreaViewSet, basename='service-areas')

urlpatterns = [
    path('', include(router.urls))
]
