from django.contrib.gis.geos import Polygon
from rest_framework import status

from . import BaseAPITestCase, ServiceAreaFactory, ProviderFactory


class ServiceAreaFactory(BaseAPITestCase):

    def test_create_servicearea(self):
        data = {
            "name": "Majje",
            "price": "223.99",
            "geom": {
                    "type": "Polygon",
                    "coordinates": [
                    [ 
                        [77.60216, 12.91169],
                        [77.60217, 12.91167],
                        [77.60053, 12.91107],
                        [77.60225, 12.90906],
                        [77.60216, 12.91169]
                    ]
                    ]
                },
            "provider": self.provider.id
        }
        response = self.client.post('/api/service-areas/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_service_area(self):
        response = self.client.get(f'/api/service-areas/{self.servicearea.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrive_service_area_by_params(self):
        response = self.client.get(f'/api/service-areas/?lat=50.0&lng=50.0', format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_service_area(self):
        response = self.client.delete(f'/api/service-areas/{self.servicearea_2.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_service_area(self):
        provider = ProviderFactory(
            email="monday@gmail.com"
        )
        data = {
            "name": "Majje",
            "price": "223.99",
            "geom": {
                    "type": "Polygon",
                    "coordinates": [
                    [ 
                        [77.60216, 12.91169],
                        [77.60217, 12.91167],
                        [77.60053, 12.91107],
                        [77.60225, 12.90906],
                        [77.60216, 12.91169]
                    ]
                    ]
                },
            "provider": provider.id
        }
        response = self.client.put(f'/api/service-areas/{self.servicearea_2.id}/', data=data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
