from django.db import models

# Create your models here.
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Info(models.Model):

	name = models.CharField(max_length = 20)
	class_id = models.CharField(max_length = 50,blank = True)
	address = models.CharField(max_length = 50,blank = True)
	people = models.CharField(max_length = 10,blank = True)
	student_id = models.CharField(max_length = 20,unique = True,blank = True)
	phone = models.CharField(max_length = 12)
	email = models.CharField(max_length = 20,blank = True)
	birth_place = models.CharField(max_length = 20,blank = True)
	hobby = models.CharField(max_length = 50,blank = True)
	project = models.CharField(max_length = 30,blank = True)
	is_adjusted = models.BooleanField(default = True)
	interview_time = models.TextField(max_length = 50,blank = True)
	advantages = models.TextField(blank = True)
	gains = models.TextField(blank = True)
	hope = models.TextField(blank = True)












