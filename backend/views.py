from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.utils.decorators import method_decorator

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets


from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


@method_decorator(
    name='list', 
    decorator=swagger_auto_schema(
        operation_description="description from swagger_auto_schema via method_decorator",
        manual_parameters=[
            openapi.Parameter('lat', openapi.IN_QUERY, "latitude", type=openapi.TYPE_STRING),
            openapi.Parameter('lng', openapi.IN_QUERY, "longitude", type=openapi.TYPE_STRING)
        ]
))
class ServiceAreaViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        queryset = ServiceArea.objects.all()
        latitude = self.request.query_params.get('lat')
        longitude = self.request.query_params.get('lng')
        
        if (latitude and longitude):
            pnt = Point(float(latitude), float(longitude), srid=4326)
            queryset = queryset.filter(geom__covers=pnt)
        return queryset
