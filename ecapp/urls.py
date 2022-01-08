from django.urls import path

from ecapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
