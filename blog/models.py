from django.db import models

# Create your models here.
class Text(models.Model):

    title = models.CharField(max_length = 32)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True, blank = True)
    tag = models.CharField(max_length = 32)
  