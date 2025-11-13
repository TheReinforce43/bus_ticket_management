from django.urls import path ,include 

from rest_framework.routers import DefaultRouter

from location.View.location_view import ServiceDistrictViewSet

router = DefaultRouter() 

router.register(r'service-districts',ServiceDistrictViewSet,basename='service-districts')


urlpatterns = [
    path('',include(router.urls)),
]
