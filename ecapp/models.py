from django.db import models
from django.contrib.gis.db import models

class WeatherTask(models.Model):
    cord = models.CharField(max_length=200,blank=True,null=True)
    name = models.CharField(max_length=100, blank=False,null=True)
    location = models.PointField(null=True,blank=True)
    temp = models.CharField(max_length=200,blank=True,null=True)
    humidit_validtime = models.CharField(max_length=200,blank=True,null=True)
    humidit_value = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200,blank=True,null=True)
    state = models.CharField(max_length=200,blank=True,null=True)
    timezone_c = models.CharField(max_length=200,blank=True,null=True)
    desc = models.CharField(max_length=200,blank=True,null=True)
    temp_windDirection = models.CharField(max_length=200,blank=True,null=True)
    temp_windSpeed = models.CharField(max_length=200,blank=True,null=True)
    temp_temperatureUnit = models.CharField(max_length=200,blank=True,null=True)
    temp_isDaytime = models.CharField(max_length=200,blank=True,null=True)
    temp_endTime = models.CharField(max_length=200,blank=True,null=True)
    temp_startTime = models.CharField(max_length=200,blank=True,null=True)
    detailedforecastDesc = models.TextField(blank=True,null=True)
    img = models.URLField(max_length=250,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'WeatherTask'
