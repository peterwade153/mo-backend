from rest_framework import status

from . import BaseAPITestCase, ProviderFactory


class ProviderTestCase(BaseAPITestCase):

    def test_create_provider(self):
        data = {
            "name": "lason james",
            "email": "lason@gmail.com",
            "phone_number": "+1234234567",
            "language": "en",
            "currency": "USD"
            }
        response = self.client.post('/api/providers/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_provider(self):
        response = self.client.get(f'/api/providers/{self.provider.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_provider(self):
        provider = ProviderFactory(
            email="today@gmail.com"
        )
        data = {
            "name": "qurty james",
            "email": "lobaton@gmail.com",
            "phone_number": "+123423967",
            "language": "eS",
            "currency": "EUR"
        }
        response = self.client.put(f'/api/providers/{provider.id}/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_provider(self):
        provider = ProviderFactory(
            email="monday@gmail.com"
        )
        response = self.client.delete(f'/api/providers/{provider.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
