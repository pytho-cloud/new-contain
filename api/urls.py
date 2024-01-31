from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib import admin
from django.urls import path ,include 
from rest_framework.routers import DefaultRouter 
from .views import UserViewset
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializer import (
#     CustomUserSerializer,
#     VerifyUserSerializer,
#     ForgetPasswordSerializer,
# )
# from .models import CustomUser
# # from .email import send_mail_via_email, send_forget_password_mail

# # Create your views here.


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def registration_view(request):
#     print(request.data)
#     serializer = CustomUserSerializer(data=request.data)

#     if serializer.is_valid():
#         user = serializer.save()
#         print(user)
#         email = serializer.data["email"]
#         # send_email = send Mail function == True if send_email is True token will generate

#         send_mail = send_mail_via_email(email)

#         if send_mail == True:
#             # refresh = RefreshToken.for_user(user)
#             return Response(
#                 {"message": "OTP send to you Email Address"},
#                 status=status.HTTP_201_CREATED,
#             )
#         return Response({"message": "something went Wrong"})
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def verify_otp(request):
#     data = request.data

#     serializer = VerifyUserSerializer(data=data)

#     if serializer.is_valid():
#         email = serializer.data["email"]
#         otp = serializer.data["otp"]
#         print(email, otp)

#         user = CustomUser.objects.filter(email=email)

#         if not user.exists():
#             Response({"status": 400, "message": "Check Your email Correctly"})

#         if not user[0].otp == otp:
#             Response({"status": 400, "message": "Enter OTP is Incorrect"})

#         user[0].is_verified == True
#         user[0].save()
#         refresh = RefreshToken.for_user(user[0])

#         return Response(
#             {
#                 "status": 200,
#                 "message": "Succuessfully registered ",
#                 "access": str(refresh.access_token),
#                 "refresh": str(refresh),
#             }
#         )


# # Forget Password View
# @api_view(["POST"])
# @permission_classes([AllowAny])
# def forget_password(request):
#     try:
#         data = request.data

#         serializer = ForgetPasswordSerializer(data=data)

#         if serializer.is_valid():
#             username = serializer.data["username"]
#             email = serializer.data["email"]

#             user = CustomUser.objects.get(email=email)

#             if not user.username == username:
#                 return Response({"message": "Username is doesn't exist", "status": 400})
#             forget_mail = send_forget_password_mail(username, email)
#             if forget_mail == True:
#                 return Response(
#                     {"message": "OTP send to you Email Address"},
#                     status=status.HTTP_201_CREATED,
#                 )
#             return Response({"message": "Please Enter Correct details"})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     except Exception as e:
#         print(e)


# # Forget Password verifictions


router = DefaultRouter()

router.register(r'user',UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include(router.urls)),
    # path('register/', registration_view, name='register'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path("verifyOtp/",verify_otp,name="verify_otp"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register_user'),

    path('user/', GetUserView.as_view(), name='get_user'),

]
