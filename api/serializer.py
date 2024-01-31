from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUserProfile
#         fields = ('id', 'username','email','subscriptions_status',)
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email', 'is_active', "is_staff")


# class VerifyUserSerializer(serializers.Serializer):

#     # username = serializers.CharField()
#     email = serializers.EmailField()



    
#     otp = serializers.CharField()

# class ForgetPasswordSerializer(serializers.Serializer):

#     username = serializers.CharField()
#     email = serializers.EmailField()
        

from rest_framework.serializers import ModelSerializer
# from api.models import CustomUserProfile

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = CustomUserProfile
#         fields = ('id', 'email', 'username','is_active', 'is_staff',)  # Add more fields as needed


class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']