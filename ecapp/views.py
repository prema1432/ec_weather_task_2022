import requests
from django.contrib.gis.geos import Point, WKBWriter
from django.shortcuts import render
from django.contrib import messages

from ecapp.models import WeatherTask
from django.views.generic.base import TemplateView


def index(request):
    context = {}
    get_points_url = "https://api.weather.gov/points/"
    if request.method == 'POST':
        if request.POST.get('cord'):
            try:
                cord = request.POST.get('cord')
                pointsRes = requests.get(get_points_url + cord).json()
                lan=pointsRes['geometry']
                lan2=pointsRes['properties']
                city = pointsRes['properties']['relativeLocation']['properties']['city']
                state = pointsRes['properties']['relativeLocation']['properties']['state']
                timezone_country = pointsRes['properties']['timeZone']
                hourlyRes = requests.get(
                    pointsRes['properties']["forecast"]).json()
                hourlyRes2 = requests.get(
                    pointsRes['properties']["forecastGridData"]).json()
                humidit_uom = hourlyRes2['properties']['relativeHumidity']['uom']
                humidit_validtime = hourlyRes2['properties']['relativeHumidity']['values'][0]['validTime']
                humidit_value = hourlyRes2['properties']['relativeHumidity']['values'][0]['value']
                temp = hourlyRes["properties"]['periods'][0]['temperature']
                img = hourlyRes["properties"]['periods'][0]['icon']
                lop = hourlyRes2['properties']['temperature']['values'][0]['validTime'][0:19]
                temp_name = hourlyRes["properties"]['periods'][0]['name']
                temp_startTime = hourlyRes["properties"]['periods'][0]['startTime']
                temp_endTime = hourlyRes["properties"]['periods'][0]['endTime']
                temp_isDaytime = hourlyRes["properties"]['periods'][0]['isDaytime']
                temp_temperatureUnit = hourlyRes["properties"]['periods'][0]['temperatureUnit']
                temp_windSpeed = hourlyRes["properties"]['periods'][0]['windSpeed']
                temp_windDirection = hourlyRes["properties"]['periods'][0]['windDirection']
                shortDesc = hourlyRes["properties"]['periods'][0]['shortForecast']
                detailedforecastDesc = hourlyRes["properties"]['periods'][0]['detailedForecast']
                messages.success(request, 'Data Fetched Successfully')
                WeatherTask.objects.get_or_create(cord=cord,name=temp_name,location=Point(40.8471,-93.8679),temp=temp,humidit_validtime=humidit_validtime,humidit_value=humidit_value,city=city,state=state,timezone_c=timezone_country,desc=shortDesc,temp_windDirection=temp_windDirection,temp_windSpeed=temp_windSpeed,temp_temperatureUnit=temp_temperatureUnit,temp_isDaytime=temp_isDaytime,temp_endTime=temp_endTime,temp_startTime=temp_startTime,detailedforecastDesc=detailedforecastDesc,img=img)
                # WeatherTask.objects.get_or_create(cord=cord,name=temp_name,temp=temp,humidit_validtime=humidit_validtime,humidit_value=humidit_value,city=city,state=state,timezone_c=timezone_country,desc=shortDesc,temp_windDirection=temp_windDirection,temp_windSpeed=temp_windSpeed,temp_temperatureUnit=temp_temperatureUnit,temp_isDaytime=temp_isDaytime,temp_endTime=temp_endTime,temp_startTime=temp_startTime,detailedforecastDesc=detailedforecastDesc,img=img)
                context = {
                    'cord': cord,
                    'humidit_uom': humidit_uom,
                    'humidit_validtime': humidit_validtime,
                    'humidit_value': humidit_value,
                    'city': city,
                    'state': state,
                    'timezone_c': timezone_country,
                    'temp': temp,
                    'img': img,
                    'desc': shortDesc,
                    'temp_name': temp_name,
                    'temp_windDirection': temp_windDirection,
                    'temp_windSpeed': temp_windSpeed,
                    'temp_temperatureUnit': temp_temperatureUnit,
                    'temp_isDaytime': temp_isDaytime,
                    'temp_endTime': temp_endTime,
                    'temp_startTime': temp_startTime,
                    'detailedforecastDesc': detailedforecastDesc

                }
            except:
                messages.warning(request, 'Given Coordinates Data Not Available')
                return render(request, 'weather_app/index.html', context)

            return render(request, 'weather_app/index.html', context)
    else:
        return render(request, 'weather_app/index.html', context)


class MarkersMapView(TemplateView):

    template_name = "weather_app/visited_map.html"