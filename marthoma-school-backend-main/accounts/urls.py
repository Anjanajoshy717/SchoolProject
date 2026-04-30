from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts import views
from accounts.views import (
    SubadminLoginView,  # Updated view name
    StudentLoginView,
    LogoutView,
    CustomTokenRefreshView,
    ForgotPasswordView,ResetPasswordAfterOTPView,VerifyOTPView,ResendOTPView
)

app_name = "accounts"

router = DefaultRouter()
# router.register('password-reset', views.PasswordResetViewSet, basename='password-reset')

urlpatterns = [
    # Authentication
    path('subadmin-login/', SubadminLoginView.as_view(), name='subadmin-login'),  # Subadmin and Admin login via email
    path('student-login/', StudentLoginView.as_view(), name='student-login'),      # Student login via registration_number
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token-refresh'),

    # User Profile
    path('me/', views.CurrentUserView.as_view(), name='current-user'),

    # Password Reset (unauthenticated)
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('reset-password/', ResetPasswordAfterOTPView.as_view(), name='reset_password'),
    path('resend-otp/', ResendOTPView.as_view(), name='resend_otp'),

    # Password Reset using current password
    path('reset-passwords/', views.ResetPasswordView.as_view(), name='reset-password'),

    # Password reset with OTP
    path('', include(router.urls)),
]