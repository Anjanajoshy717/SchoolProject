from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    job_type = models.CharField(max_length=200)
    vacancies = models.IntegerField(default=1)
    qualification = models.CharField(max_length=200)
    job_description = models.TextField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    last_date = models.DateField()
    is_active = models.BooleanField(default=True)
    experience = models.CharField(max_length=100, blank=True, null=True) 
    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    years_of_experience = models.CharField(max_length=10)
    qualification = models.CharField(max_length=200)
    current_location = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} applied for {self.job.title}"
