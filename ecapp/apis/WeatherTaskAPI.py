from rest_framework import viewsets
from rest_framework_gis import filters

from ecapp.models import WeatherTask
from ecapp.serializers.WeatherTaskSerializer import WeatherTaskSerializer

class WeatherTaskViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = WeatherTask.objects.all()
    serializer_class = WeatherTaskSerializer