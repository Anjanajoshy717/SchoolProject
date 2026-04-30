from django.contrib import admin
from accounts.models import CustomUser,PasswordResetOTP

admin.site.register(CustomUser)
admin.site.register(PasswordResetOTP)
