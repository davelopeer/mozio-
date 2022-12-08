from rest_framework import viewsets
from area.models import ServiceArea
from area.api.serializers import ServiceAreaSerializer
from django.http import JsonResponse
from geopy.geocoders import Nominatim

class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class FindPolygonsViewSet(viewsets.ViewSet):
  allowed_methods = ['GET', 'OPTIONS'] 
  queryset = ServiceArea.objects.all()

  def list(self, request):
    if 'lat' not in request.query_params.keys() or 'lng' not in request.query_params.keys():
      return JsonResponse({'error': 'provide a valide lat and lng'})
    lat = request.query_params['lat']
    lng = request.query_params['lng']
    geolocator = Nominatim(user_agent="service_area")
    location = geolocator.reverse(f'{lat}, {lng}')

    return JsonResponse({'location': location.raw['address']})
    