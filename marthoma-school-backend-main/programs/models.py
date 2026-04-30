from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Event(models.Model):
    STATUS_CHOICES = (
        ("upcoming", "Upcoming"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("Ongoing", "Ongoing")  # Changed 'Ongoing' to lowercase for consistency
    )
    CATEGORIES_CHOICES = (
        ("Academic", "Academic"),
        ("Sports", "Sports"), # The Sports category will now contain winner information
        ("Cultural", "Cultural"),
        ("Administrative", "Administrative"),
        ("Technology", "Technology"),
        ("Arts", "Arts"),
        ("Community Service", "Community Service"),
        ("Workshop", "Workshop"),
        ("Competition", "Competition"),
        ("Celebration", "Celebration"),
    )
    ORGANIZERS_CHOICES = (
        ("Administration", "Administration"),
        ("Academic Department", "Academic Department"),
        ("Arts Department", "Arts Department"),
        ("Sports Department", "Sports Department"),
        ("Science Department", "Science Department"),
        ("Student Council", "Student Council"),
        ("Parent Association", "Parent Association"),
        ("Technology Club", "Technology Club"),
        ("Cultural Club", "Cultural Club"),
        ("Community Service Club", "Community Service Club"),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    event_date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    organizer = models.CharField(max_length=50, choices=ORGANIZERS_CHOICES , default="Administration")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="upcoming")
    category = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, default="Academic")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'description')

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="event_images/", storage=MediaCloudinaryStorage())

    def __str__(self):
        return f"Image for {self.event.title}"

class Winner(models.Model):
    POSITION_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
    ]
    event = models.ForeignKey(Event, related_name='winners', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='winner_photos/', storage=MediaCloudinaryStorage())
    student_class = models.CharField(max_length=20)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.position})"