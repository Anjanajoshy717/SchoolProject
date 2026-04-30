from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser

# Removed the RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
    """General user serializer for various responses"""
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'role',
            'is_active',
            'registration_number'
        ]


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    # new_password = serializers.CharField(min_length=6)

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(min_length=6)

class SubadminLoginSerializer(TokenObtainPairSerializer):
    # This serializer now specifically handles Subadmin login
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = CustomUser.objects.filter(email=email).first()

            if not user or not user.check_password(password):
                raise AuthenticationFailed("Invalid email or password.")
            
            # Subadmin and Admin login should use email
            if user.role not in ['admin', 'subadmin']:
                raise AuthenticationFailed("Access denied for this role. Only Admins and Subadmins can log in via email.")
            
            if not user.is_active:
                raise AuthenticationFailed("User account is inactive.")

            self.user = user
            
            # Continue with token generation after successful validation
            data = super().validate(attrs)
            
            # Add user details to the response
            data["user"] = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "email": user.email,
                "role": user.role,
                "is_active": user.is_active,
            }
            return data
        else:
            raise serializers.ValidationError('Must include "email" and "password".')

# accounts/serializers.py (UPDATED)

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser

class StudentLoginSerializer(TokenObtainPairSerializer):
    username_field = 'registration_number'

    # The validate method should be simplified
    def validate(self, attrs):
        # The parent method handles the authentication.
        # It uses the CustomAuthBackend to find the user by registration_number.
        data = super().validate(attrs)

        # After authentication, add your custom role check
        user = self.user
        if user.role != 'student':
            raise AuthenticationFailed("Access denied. Only students can log in with a registration number.")

        # If all checks pass, add the user details to the response
        data["user"] = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
            "email": user.email,
            "role": user.role,
            "is_active": user.is_active,
            "registration_number": user.registration_number,
        }
        return data