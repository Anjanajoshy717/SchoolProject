from django.core.management.base import BaseCommand
from django.utils import timezone
from job.models import Job  # Replace 'your_app_name' with your actual app name

class Command(BaseCommand):
    help = 'Checks for jobs where the last date has passed and sets is_active to False.'

    def handle(self, *args, **options):
        # Get the current date (without time)
        today = timezone.now().date()
        
        # Find active jobs where the last_date is less than today
        expired_jobs = Job.objects.filter(last_date__lt=today, is_active=True)
        
        # Update the jobs to be inactive
        if expired_jobs.exists():
            count = expired_jobs.update(is_active=False)
            self.stdout.write(self.style.SUCCESS(f'Successfully closed {count} expired jobs.'))
        else:
            self.stdout.write(self.style.SUCCESS('No expired jobs to close.'))