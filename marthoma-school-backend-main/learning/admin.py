from django.contrib import admin
from .models import Subject,Section,Syllabus,SyllabusPart
# Register your models here.
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Syllabus)
admin.site.register(SyllabusPart)