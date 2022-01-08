from rest_framework_gis import serializers
from ecapp.models import WeatherTask


class WeatherTaskSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        fields = ("id", "name","city","temp","humidit_value")
        geo_field = "location"
        model = WeatherTask