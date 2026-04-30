"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from accounts.views import CustomTokenObtainPairView,LogoutView,CustomTokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('programs.urls')),
    path('api/', include('teachers.urls')),
    path('api/', include('enquiry.urls')),
    path('api/', include('facility.urls')),
    path('api/',include('learning.urls')),
    path('api/',include('job.urls')),
    path('api/', include('reviews.urls')),
    path('api/', include('Sports.urls')),
    path('api/', include('advertisement.urls')),
    path('about-us/', include("AboutUs.urls")),
    path('api/news/', include('news.urls')),
    path('api/', include('achivements.urls')),
    path('api/', include('students.urls')),
path('api/', include('school.urls')),
    # path('api/', include('career.urls')),
    # path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    # path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/auth/token/refresh/', CustomTokenRefreshView.as_view(), name='custom_token_refresh'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)