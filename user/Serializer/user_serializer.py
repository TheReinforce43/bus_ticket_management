from rest_framework import serializers 
# from user.models import User 

from django.contrib.auth import authenticate , get_user_model

from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


# User Sign Up Serializer 


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'image']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

# this serializer is for user login 


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True) 
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)



    def validate(self,attrs):

        email = attrs.get('email')
        password = attrs.get('password') 


        if not email or not password:
            raise serializers.ValidationError("Email and password are required to login.")
        
        user = authenticate(email=email, password=password)

        if not user :
            raise serializers.ValidationError("Invalid email or password.")
        
        # Now generate JWT tokens for the authenticated user 

        refresh_token = RefreshToken.for_user(user) 

        return  {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
        }
        


# this serializer is used for logout 


class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            refresh_token = RefreshToken(self.token)
            refresh_token.blacklist()
        except Exception as e:
            raise serializers.ValidationError("Invalid token or token has already been blacklisted.")

    