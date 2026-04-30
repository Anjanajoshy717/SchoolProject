from django.db import models
from django.db.models.fields.related import ForeignKey
from cloudinary_storage.storage import MediaCloudinaryStorage

class Achievements(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AchievementImage(models.Model):
    achievement = ForeignKey(Achievements, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='achievements/images/', storage=MediaCloudinaryStorage())
    
    def __str__(self):
        return f"Image for {self.achievement.title}"