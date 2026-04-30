from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

# Create your models here.
class SportEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Winner(models.Model):
    POSITION_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
    ]
    event = models.ForeignKey(SportEvent, related_name='winners', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='winner_photos/', storage=MediaCloudinaryStorage())
    student_class = models.CharField(max_length=20)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.position})"

class SportImage(models.Model):
    event = models.ForeignKey(SportEvent, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sports_images/', storage=MediaCloudinaryStorage())

    def __str__(self):
        return f"Image for {self.event.title}"

