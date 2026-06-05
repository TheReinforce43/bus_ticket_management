from rest_framework.viewsets import ModelViewSet 

from location.Model.location_model import ServiceDistrictModel
from location.Serializer.loation_serializer import (
    CreateServiceDistrictSerializer,
    ServiceDistrictDetailSerializer
)

from support_function.custom_permission import DistrictServiceObjectPermission
from django.core.cache import cache 

from bus_ticket_project.settings import CACHE_TTL

from rest_framework.response import Response 
from rest_framework import status 


DISTRICT_CACHE_KEY = "service_district_{id}"
DISTRICT_LIST_CACHE_KEY = "service_district_list"

class ServiceDistrictViewSet(ModelViewSet):
    queryset = ServiceDistrictModel.objects.select_related('responsiblePerson')
    permission_classes = [DistrictServiceObjectPermission]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ServiceDistrictDetailSerializer
        return CreateServiceDistrictSerializer

    def list(self,request, *args, **kwargs):
        cached_data = cache.get(DISTRICT_LIST_CACHE_KEY)
        if cached_data:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(DISTRICT_LIST_CACHE_KEY, response.data, timeout=3600)  # Cache for 1 hour
        return response

    def retrieve(self, request, *args, **kwargs):
        cache_key = DISTRICT_CACHE_KEY.format(id=kwargs['pk'])
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        response = super().retrieve(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=CACHE_TTL)
        return response

    def _invalidate_cache(self, pk=None):
        cache.delete(DISTRICT_LIST_CACHE_KEY)
        if pk:
            cache.delete(DISTRICT_CACHE_KEY.format(id=pk))


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        self._invalidate_cache()
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        self._invalidate_cache(pk=kwargs['pk'])
        return response

    def destroy(self, request, *args, **kwargs):
        self._invalidate_cache(pk=kwargs['pk'])
        return super().destroy(request, *args, **kwargs)
    
