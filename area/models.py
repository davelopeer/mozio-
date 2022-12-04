from django.db import models

# Create your models here.
class ServiceArea(models.Model):
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  geojson_information = models.CharField(max_length=10000)