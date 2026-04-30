from django.db import models
from django.conf import settings
from cloudinary_storage.storage import MediaCloudinaryStorage

class Teacher(models.Model):
    # Link to the CustomUser model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')

    CATEGORY_CHOICES = (
        ('active', 'active'),
        ('retired', 'retired'),
        ('deceased', 'deceased'),
    )

    name = models.CharField(blank=True, null=True, max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    experience = models.PositiveIntegerField(blank=True, null=True, default=0)
    degree = models.CharField(max_length=200, blank=True, null=True)
    college_or_uni = models.CharField(max_length=150, null=True, blank=True)
    yearofpass = models.PositiveBigIntegerField(blank=True, null=True)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='active',
    )
    subject = models.CharField(max_length=200, blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='teachers/profile_pics/', blank=True, null=True, storage=MediaCloudinaryStorage())

    def __str__(self):
        if self.user:
            return str(self.user)
        return f"Teacher (ID: {self.pk})"


    class Meta:
        ordering = ['name']

class teachersprofview(models.Model):
    teachers_name=models.CharField(null=True,blank=True,max_length=100)
    tittle=models.TextField(null=True,blank=True)
    description=models.CharField(max_length=300,null=True,blank=True)
    prof_pic=models.ImageField(upload_to='teachers/prof_pic/', null=True,blank=True, storage=MediaCloudinaryStorage())
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teachers_name