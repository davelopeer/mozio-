from rest_framework import serializers
from area.models import ServiceArea


class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceArea
        fields = [
          'name',
          'price',
          'geojson_information',
        ]