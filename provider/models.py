from django.db import models

# Create your models here.
class Provider(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phone_number = models.CharField(max_length=255)
  language = models.CharField(max_length=255)
  currency = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.name