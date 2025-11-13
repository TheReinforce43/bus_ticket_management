from rest_framework.viewsets import ModelViewSet 
from location.Model.location_model import ServiceDistrictModel
from location.Serializer.loation_serializer import (
    CreateServiceDistrictSerializer,
    ServiceDistrictDetailSerializer
)

from support_function.custom_permission import DistrictServiceObjectPermission



class ServiceDistrictViewSet(ModelViewSet):
    queryset = ServiceDistrictModel.objects.select_related('responsiblePerson')
    permission_classes = [DistrictServiceObjectPermission]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ServiceDistrictDetailSerializer
        return CreateServiceDistrictSerializer
    
