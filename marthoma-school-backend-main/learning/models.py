from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage


class Subject(models.Model):
    class_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="subject_images/", blank=True, null=True, storage=MediaCloudinaryStorage())
    subject_id = models.IntegerField(default=1)

    class Meta:
        unique_together = ('class_id', 'subject_id')

    def __str__(self):
        return f"Class {self.class_id} - {self.name}"


class Section(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="sections", blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    unit_id = models.IntegerField(default=1)
    image = models.ImageField(upload_to="section_images/", blank=True, null=True, storage=MediaCloudinaryStorage())

    class Meta:
        unique_together = ('subject', 'unit_id')

    def __str__(self):
        return f"{self.subject.name if self.subject else 'No Subject'} - {self.title}"


class Syllabus(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="syllabus", blank=True, null=True)
    chapter_title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    syllabus_id = models.IntegerField(default=1)
    image = models.ImageField(upload_to="syllabus_images/", blank=True, null=True, storage=MediaCloudinaryStorage())

    class Meta:
        unique_together = ('section', 'syllabus_id')

    def __str__(self):
        return f"{self.section.title if self.section else 'No Section'} - {self.chapter_title}"

class SyllabusPart(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name="parts")
    part_id = models.IntegerField(default=1)
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="syllabus_parts_images/", blank=True, null=True, storage=MediaCloudinaryStorage())
    video_url = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = ('syllabus', 'part_id')
    def __str__(self):
        return f"{self.syllabus.chapter_title} - Part {self.id}"

