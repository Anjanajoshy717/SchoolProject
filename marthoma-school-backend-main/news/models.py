from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True, storage=MediaCloudinaryStorage())
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
