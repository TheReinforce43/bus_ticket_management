from rest_framework import serializers 

from location.Model.location_model import ServiceDistrictModel 
from user.Serializer.user_serializer import UserProfileSerializer    



# create location serializer
class CreateServiceDistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceDistrictModel
        fields = '__all__'


# location detail serializer
class ServiceDistrictDetailSerializer(serializers.ModelSerializer):
    responsiblePerson = UserProfileSerializer(read_only=True,many=False)

    class Meta:
        model = ServiceDistrictModel
        fields = '__all__'

