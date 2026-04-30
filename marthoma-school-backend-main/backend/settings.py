
from pathlib import Path
from decouple import config, Csv
from datetime import timedelta
import cloudinary
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SESSION_COOKIE_SECURE = False

# Quick-start development settings - unsuitable for production
SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)
ENV = config("ENV", default="development")
IS_DEV = ENV == "development"

CORS_ALLOW_CREDENTIALS = True
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())
AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.CustomAuthBackend',
    
]

# ------------------ REST Framework ------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
}

# ------------------ EMAIL SETTINGS ------------------
# Commenting out real SMTP for testing
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'swebaraj17@gmail.com'
EMAIL_HOST_PASSWORD = 'qleu owqh aksa qtul'  # Gmail app password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
"""

# Using console backend for OTP/email testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'your-email@example.com'

# ------------------ CORS ------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://marthoma-high-school.netlify.app",
    "https://marthoma.netlify.app",
    "http://marthomaschoolkuriannoor.com",
    "https://marthomaschoolkuriannoor.com",
]

# ------------------ SIMPLE JWT ------------------
SIMPLE_JWT = {
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_COOKIE": "refresh_token",
    "AUTH_COOKIE_PATH": "/api/auth/token/refresh/",
    "AUTH_COOKIE_HTTP_ONLY": True,
    "AUTH_COOKIE_SECURE": False,
    "AUTH_COOKIE_SAMESITE": "Lax",
    "BLACKLIST_AFTER_ROTATION": True,
    "ROTATE_REFRESH_TOKENS": True,
}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'programs',
    'accounts',
    'teachers',
    'enquiry',
    'learning',
    'facility',
    'job',
    'reviews',
    'Sports',
    'news',
    'AboutUs',
    'advertisement',
    'achivements',
    'students',
    'cloudinary_storage',
    'cloudinary','school'
]

# Cloudinary Settings
CLOUDINARY_CLOUD_NAME = "dunlntdy3"
CLOUDINARY_API_KEY = "454341219174761"
CLOUDINARY_API_SECRET = "NIhM0PgdElTPwPg6dZr2LQmBprE"
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dunlntdy3',
    'API_KEY': '454341219174761',
    'API_SECRET': 'NIhM0PgdElTPwPg6dZr2LQmBprE',
}
# Set Cloudinary as the default storage backend for media files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ------------------ STATIC FILES ------------------
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# ------------------ MIDDLEWARE ------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',  # Disabled for API
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neondb',
        'USER': 'neondb_owner',
        'PASSWORD': 'npg_T4I0DakLmCvB', # Use the correct password from your connection string
        'HOST': 'ep-spring-breeze-a1qjrwqi-pooler.ap-southeast-1.aws.neon.tech',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
        'CONN_MAX_AGE': 600,
    }
}
# ------------------ PASSWORD VALIDATION ------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ------------------ INTERNATIONALIZATION ------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'zecserbusiness@gmail.com'
EMAIL_HOST_PASSWORD = 'wlsx ausq sxkm qxhr'  # Gmail app password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# ------------------ DEFAULT PK FIELD ------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


