from rest_framework import viewsets
from area.models import ServiceArea
from area.api.serializers import ServiceAreaSerializer

class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer