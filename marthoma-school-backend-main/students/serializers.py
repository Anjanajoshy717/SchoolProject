from rest_framework import serializers
from django.contrib.auth import get_user_model # ✅ Use this instead
from .models import Student, CLASS_CHOICES, GENDER_CHOICES
from django.core.mail import send_mail  
from django.conf import settings

CustomUser = get_user_model() # ✅ Get the actual model class

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser # ✅ This now correctly references the model class
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'phone_number',
            'password', 
            'registration_number' 
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': False, 'allow_blank': True},
            'phone_number': {'required': False, 'allow_blank': True},
            'registration_number': {'required': True}, 
        }

class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Student
        fields = [
            'id', 
            'user', 
            'student_class', 
            'section', 
            'date_of_birth', 
            'gender', 
            'guardian_name', 
            'address', 
            'profile_picture'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        
        user = CustomUser.objects.create_user(
            password=password, 
            role='student',
            is_active=True, 
            **user_data
        )
        
        student = Student.objects.create(user=user, **validated_data)
        subject = 'Welcome to Student Portal!'
        message = (
            f'Dear {user.first_name},\n\n'
            f'Welcome to Marthoma School Student Portal! Your account has been created successfully.\n'
            f'You can now log in to the student portal using the following details:\n\n'
            f'Registration Number: {user.registration_number}\n'
            f'Password: {password}\n\n'
            f'For security, we recommend you change this password on your first login.\n\n'
            f'Thank you,\n'
            f'The Marthoma School Team'
        )
        
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],  # ✅ The recipient is the student's email
                fail_silently=False,
            )
        except Exception as e:
            # Handle the error gracefully if the email fails to send
            print(f"Failed to send welcome email to {user.email}: {e}")

        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.email = user_data.get('email', user.email)
        user.phone_number = user_data.get('phone_number', user.phone_number)
        user.registration_number = user_data.get('registration_number', user.registration_number)
        if 'password' in user_data and user_data['password']:
            user.set_password(user_data['password'])
        user.save()

        instance.student_class = validated_data.get('student_class', instance.student_class)
        instance.section = validated_data.get('section', instance.section)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.guardian_name = validated_data.get('guardian_name', instance.guardian_name)
        instance.address = validated_data.get('address', instance.address)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        
        return instance