from django.contrib import admin
from blog import models

# Register your models here.

class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag','create_time')
    
admin.site.register(models.Text, TextAdmin)
