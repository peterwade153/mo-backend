from django.contrib.gis.db import models
from django.core.validators import RegexValidator

from app.settings.base import LANGUAGE_CODE


# Validators
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='please enter phonenumber in the format +123123123, upto 15 digits allowed!',
    code='Invalid phone'
)

class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    language = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    geom = models.PolygonField(blank=True, null=True)
