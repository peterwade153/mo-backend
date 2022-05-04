import factory
from django.contrib.gis.geos import Polygon
from rest_framework.test import APITestCase

from backend.models import Provider, ServiceArea


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provider


class ServiceAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceArea


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.provider = ProviderFactory()
        self.servicearea = ServiceAreaFactory(
            provider=self.provider,
            name='Boston',
            price='234.99',
            geom=Polygon( ((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0,0.0)) )
        )
        self.servicearea_2 = ServiceAreaFactory(
            provider=self.provider,
            name='Boston-celtics',
            price='234.45',
            geom=Polygon( ((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0,0.0)) )
        )
