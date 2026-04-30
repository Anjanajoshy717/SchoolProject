from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Event,EventImage,Winner

# Register your models here.
admin.site.register(Event)
admin.site.register(EventImage)
admin.site.register(Winner)