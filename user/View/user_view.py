from rest_framework.views import APIView 
from rest_framework.generics import CreateAPIView 
from rest_framework.response import Response 
from rest_framework import status 
from  django.contrib.auth import get_user_model 
from  user.Serializer.user_serializer import (
    UserSignUpSerializer,
    UserLoginSerializer,
    UserLogoutSerializer
)

User = get_user_model()

from rest_framework.permissions import AllowAny

# User Sign Up Serializer 


class UserSignUpAPIView(CreateAPIView):
    serializer_class= UserSignUpSerializer
    queryset= User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self,request,*args,**kwargs):

        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data,status=status.HTTP_200_OK)
    
class UserLogoutAPIView(APIView):
    

    def post(self,request,*args,**kwargs):

        serializer = UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message":"Successfully logged out."},status=status.HTTP_200_OK)




