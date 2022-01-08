from rest_framework import routers

from ecapp.apis.WeatherTaskAPI import WeatherTaskViewSet

router = routers.DefaultRouter()
router.register(r"ecapp", WeatherTaskViewSet)

urlpatterns = router.urls