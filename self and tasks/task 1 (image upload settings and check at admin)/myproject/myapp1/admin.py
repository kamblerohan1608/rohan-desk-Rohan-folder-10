from django.contrib import admin
from .models import myappModel

# Register your models here.

@admin.register(myappModel)
class myappAdminModel(admin.ModelAdmin):
    list_display = ['image_title','image_description','image_photo']
