from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from cloudinary_storage.storage import MediaCloudinaryStorage


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/',null=True, storage=MediaCloudinaryStorage())
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, help_text="Optional: External link")
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_current(self):
        today = timezone.now().date()
        return self.is_active and self.start_date <= today <= self.end_date
