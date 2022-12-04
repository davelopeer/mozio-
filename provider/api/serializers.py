from rest_framework import serializers
from provider.models import Provider


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = [
          'name',
          'email',
          'phone_number',
          'language',
          'currency',
        ]