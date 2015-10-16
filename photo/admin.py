from django.contrib import admin
from photo import models

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(models.Photo, PhotoAdmin)
