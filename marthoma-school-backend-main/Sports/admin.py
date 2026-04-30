from django.contrib import admin
from .models import SportEvent, Winner, SportImage

# Register your models here.
admin.site.register(SportEvent)
admin.site.register(Winner)
admin.site.register(SportImage)
