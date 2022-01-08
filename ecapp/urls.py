from django.urls import path

from ecapp import views
from ecapp.views import MarkersMapView

urlpatterns = [
    path('', views.index, name='index'),
    path("visited_map/", MarkersMapView.as_view()),

]
