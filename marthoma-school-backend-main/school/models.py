from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class SchoolPhoto(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='school_photos/',
        storage=MediaCloudinaryStorage()
    )

    def __str__(self):
        return self.title