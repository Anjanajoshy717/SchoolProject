# accounts/views.py
import random
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .serializers import (
    SubadminLoginSerializer,
    StudentLoginSerializer,
    UserSerializer,
    PasswordResetRequestSerializer,
    OTPVerificationSerializer,PasswordResetSerializer
)
from .models import CustomUser, PasswordResetOTP

# ----- CURRENT USER -----
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
            "email": user.email,
            "role": user.role,
            "is_active": user.is_active,
            "registration_number": user.registration_number,
        })


# ----- SUBADMIN LOGIN (email + password) -----
@method_decorator(csrf_exempt, name='dispatch')
class SubadminLoginView(TokenObtainPairView):
    serializer_class = SubadminLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data['refresh']

        response = Response(serializer.validated_data)
        response.set_cookie(
            key=settings.SIMPLE_JWT.get('AUTH_COOKIE', 'refresh_token'),
            value=refresh_token,
            httponly=True,
            secure=False,
            samesite='Lax',
            path='/api/token/refresh/',
            max_age=60 * 60 * 24 * 7  # 7 days
        )
        return response


# ----- STUDENT LOGIN (registration_number + password) -----
@method_decorator(csrf_exempt, name='dispatch')
class StudentLoginView(TokenObtainPairView):
    serializer_class = StudentLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data['refresh']

        response = Response(serializer.validated_data)
        response.set_cookie(
            key=settings.SIMPLE_JWT.get('AUTH_COOKIE', 'refresh_token'),
            value=refresh_token,
            httponly=True,
            secure=False,
            samesite='Lax',
            path='/api/token/refresh/',
            max_age=60 * 60 * 24 * 7  # 7 days
        )
        return response


# ----- REFRESH TOKEN -----
class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT.get('AUTH_COOKIE', 'refresh_token'))
        if not refresh_token:
            raise AuthenticationFailed('Authentication credentials were not provided.')

        serializer = self.get_serializer(data={'refresh': refresh_token})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


# ----- LOGOUT -----
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)
        response.delete_cookie(
            key=settings.SIMPLE_JWT.get('AUTH_COOKIE', 'refresh_token'),
            path='/api/token/refresh/'
        )
        return response


# ----- FORGOT PASSWORD (SEND OTP) -----
class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = str(random.randint(100000, 999999))

            PasswordResetOTP.objects.create(email=email, otp=otp)

            # try:
            #     send_mail(
            #         subject='🔐 Password Reset OTP',
            #         message=f'Your OTP is: {otp}',
            #         from_email=settings.EMAIL_HOST_USER,
            #         recipient_list=[email],
            #         fail_silently=False,
            #     )
            try:
                send_mail(
                    subject='Your Password Reset Request',
                    message=f'Dear User,\n\n'
                            f'We received a request to reset the password for your account.\n\n'
                            f'Your One-Time Password (OTP) is: {otp}\n\n'
                            f'This OTP is valid for 10 minutes. For your security, do not share this code with anyone.\n\n'
                            f'If you did not request a password reset, you can safely ignore this email. No changes have been made to your account.\n\n'
                            f'Thank you,\n'
                            f'The Marthoma School Team',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
            except Exception as e:
                return Response({'error': f'Failed to send OTP: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'message': '✅ OTP sent successfully to email'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ------------Resendotp------------

class ResendOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            # Check if an OTP was recently sent (e.g., within the last 60 seconds)
            recent_otp = PasswordResetOTP.objects.filter(
                email=email,
                created_at__gt=timezone.now() - timedelta(seconds=60)
            ).first()
            
            if recent_otp:
                return Response(
                    {'error': 'Please wait before requesting a new OTP.'}, 
                    status=status.HTTP_429_TOO_MANY_REQUESTS
                )

            otp = str(random.randint(100000, 999999))
            
            # Create a new OTP record
            PasswordResetOTP.objects.create(email=email, otp=otp)
            
            try:
                # send_mail(
                #     subject='Your New Password Reset OTP',
                #     message=f'Your new OTP is: {otp}',
                #     from_email=settings.EMAIL_HOST_USER,
                #     recipient_list=[email],
                #     fail_silently=False,
                # )
                send_mail(
                    subject='Your Password Reset Request',
                    message=f'Dear User,\n\n'
                            f'You recently requested a new One-Time Password (OTP) to reset your password.\n\n'
                            f'Your new OTP is: **{{ otp }}**\n\n'
                            f'This code is valid for 10 minutes. For your security, please do not share this code with anyone.\n\n'
                            f'If you did not request this, please disregard this email.\n\n'
                            f'Thank you,\n'
                            f'The Marthoma School Team',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
            except Exception as e:
                return Response(
                    {'error': f'Failed to send OTP: {str(e)}'}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response(
                {'message': '✅ New OTP sent successfully to email'}, 
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ----- VERIFY OTP 

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']

            try:
                otp_obj = PasswordResetOTP.objects.filter(email=email, otp=otp).latest('created_at')
                if timezone.now() - otp_obj.created_at > timedelta(minutes=10):
                    return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)

                # You might want to delete the OTP here to prevent reuse
                # otp_obj.delete()

                return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)

            except PasswordResetOTP.DoesNotExist:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# RESET PASSWORD -----
class ResetPasswordAfterOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            new_password = serializer.validated_data['new_password']

            try:
                user = CustomUser.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)

            except CustomUser.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----- RESET PASSWORD USING CURRENT PASSWORD -----
class ResetPasswordView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # We don't need email/registration_number from request body since the user is authenticated
        current_password = request.data.get("password")
        new_password = request.data.get("new_password")
        user = request.user

        if not all([current_password, new_password]):
            return Response({"error": "Both current_password and new_password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Use the built-in check_password to verify the current password
        if not user.check_password(current_password):
            return Response({"error": "Invalid current password."}, status=status.HTTP_401_UNAUTHORIZED)

        user.set_password(new_password)
        user.save()
        return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)