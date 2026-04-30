# students/models.py

from django.db import models
from django.conf import settings
from cloudinary_storage.storage import MediaCloudinaryStorage

# Choices for Gender
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

# Choices for Class
CLASS_CHOICES = (
    ('1', 'Class 1'), ('2', 'Class 2'), ('3', 'Class 3'),
    ('4', 'Class 4'), ('5', 'Class 5'), ('6', 'Class 6'),
    ('7', 'Class 7'), ('8', 'Class 8'), ('9', 'Class 9'),
    ('10', 'Class 10'),
)

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    student_class = models.CharField(max_length=50, choices=CLASS_CHOICES)
    section = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    guardian_name = models.CharField(max_length=255)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='student_profiles/', blank=True, null=True, storage=MediaCloudinaryStorage())

    def __str__(self):
        return self.user.registration_number