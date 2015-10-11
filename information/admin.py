from django.contrib import admin

# Register your models here.
from information import models

class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'class_id','address', 'people', 'student_id','phone', 'email')
    ordering =('id',)


admin.site.register(models.Info,InfoAdmin)

