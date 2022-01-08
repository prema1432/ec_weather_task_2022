from django.contrib.gis import admin

# Register your models here.
from ecapp.models import WeatherTask

@admin.register(WeatherTask)
class MarkerAdmin(admin.OSMGeoAdmin):
    list_display = ('id','city','state','timezone_c','temp','humidit_value','location','created_at')
    date_hierarchy = 'created_at'
