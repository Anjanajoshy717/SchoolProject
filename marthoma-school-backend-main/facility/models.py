from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage


#  Our WeProvide 
class WeProvide(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='we_provide/', storage=MediaCloudinaryStorage())
    description = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.name

#  Our Facilities 
class Facility(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='facility_images/', storage=MediaCloudinaryStorage())
    description = models.TextField()

    def __str__(self):
        return self.name
