from django.db import models
from accounts.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (('admin', 'Admin'), ('subadmin', 'subadmin'),('student', 'Student'))
    REGISTRATION_NUMBER_FIELD = 'registration_number'
    otp_created_at = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True) # Set to optional
    email = models.EmailField(unique=True, null=True, blank=True) # Set to optional
    is_active = models.BooleanField(default=True) # Changed default to True
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student') # Changed default to 'student'
    otp = models.CharField(max_length=6, blank=True, null=True)
    
    # Registration number is for students
    registration_number = models.CharField(max_length=20, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'  # This is no longer the sole field for login, but Django requires it.
    REQUIRED_FIELDS = [] # Removed phone_number from required fields

    objects = UserManager()

    def __str__(self):
        # This is the correct __str__ for CustomUser.
        return self.email or self.registration_number or f"User (ID: {self.pk})"



class PasswordResetOTP(models.Model):
    email = models.EmailField(null=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.otp}"
