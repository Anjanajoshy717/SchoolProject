from rest_framework import serializers
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
# Import the model class directly from its location
from accounts.models import CustomUser

from .models import Teacher, teachersprofview

# Serializer for the CustomUser fields specific to a Teacher
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        # Use the imported class, not the string from settings
        model = CustomUser
        fields = ['email', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'phone_number': {'required': False},
        }

class TeacherSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')

        # Create the CustomUser instance with role='subadmin'
        user = CustomUser.objects.create_user(
            password=password, 
            role='subadmin', # Set the role to 'subadmin'
            is_active=True,
            is_staff=True,
            **user_data
        )

        # Create the Teacher instance and link it to the user
        teacher = Teacher.objects.create(user=user, **validated_data)
        reset_link = f'https://marthomaschoolkuriannoor.com/sub-admin/reset-password'
        subject = 'Welcome to Faculty Portal'
        message = f'Dear {teacher.name},\n\n' \
                  f'Your account has been successfully created. You can now log in using the following details:\n\n' \
                  f'Username: {user.email}\n' \
                  f'Password: {password}\n\n' \
                  f'For security, we recommend you change your password after logging in for the first time.\n\n' \
                  f'you can use this link to resetpassword'\
                  f'{reset_link}\n\n'\
                  f'Thank you,\n' \
                  f'The Marthoma School Team'
        
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
        except Exception as e:
            # Handle email sending failure (e.g., log the error)
            print(f"Failed to send welcome email to {user.email}: {e}")
        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        # Update the CustomUser fields
        user.email = user_data.get('email', user.email)
        user.phone_number = user_data.get('phone_number', user.phone_number)

        
        # Ensure is_staff remains True for teachers if not explicitly changed
        user.is_staff = user_data.get('is_staff', user.is_staff)


        if 'password' in user_data and user_data['password']:
            user.set_password(user_data['password'])
        user.save()

        # Update the Teacher profile fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

class Teachersviewserializer(serializers.ModelSerializer):
    class Meta:
        model = teachersprofview
        fields = ['id', 'teachers_name', 'tittle', 'description', 'prof_pic', 'created_at']
        read_only_fields = ['created_at']
    def update(self, instance, validated_data):
        # Handle the image update separately
        prof_pic_file = validated_data.pop('prof_pic', None)
        
        # If a new image file is provided, update the prof_pic field
        if prof_pic_file:
            instance.prof_pic = prof_pic_file
        
        # Update all other fields from the validated data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        instance.save()
        
        return instance
