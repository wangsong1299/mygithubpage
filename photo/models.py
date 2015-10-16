# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Photo(models.Model):
    DEFAULT = 'DF'
    travel = 'TR'
    song = 'WS'

    INFOTYPE_CHOICES = (
            (travel, '让心灵去旅行'),
            (song, '松鼠记录册'),
            (DEFAULT, '暂时不分类'),
    )


    title = models.CharField(max_length = 32,blank=True)
    infotype = models.CharField(max_length = 2, 
                            choices = INFOTYPE_CHOICES,
                            default = DEFAULT) 
    address = models.CharField(max_length = 32)
    reward = models.CharField(max_length = 32)
    noreward = models.CharField(max_length = 32)


