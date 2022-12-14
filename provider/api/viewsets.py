from rest_framework import viewsets
from provider.models import Provider
from provider.api.serializers import ProviderSerializer

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer