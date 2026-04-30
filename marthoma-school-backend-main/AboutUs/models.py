from django.db import models
# Create your models here.
from cloudinary_storage.storage import MediaCloudinaryStorage

class AboutUsModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="AboutUs Images", null=True, blank=True, storage=MediaCloudinaryStorage())
    description = models.TextField()
