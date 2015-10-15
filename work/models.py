# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Text(models.Model):
    DEFAULT = 'DF'
    self_work = 'SW'
    part_time = 'PT'
    full_time = 'FT'

    INFOTYPE_CHOICES = (
            (self_work, '自己闹着玩'),
            (part_time, '兼职努力做'),
            (full_time, '工作在哪里'),
            (DEFAULT, '暂时不分类'),
    )

    title = models.CharField(max_length = 32)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True, blank = True)
    infotype = models.CharField(max_length = 2, 
                                choices = INFOTYPE_CHOICES,
                                default = DEFAULT) 
    tag = models.CharField(max_length = 32)
    abstract = models.CharField(max_length = 100)
    reward = models.CharField(max_length = 32)
    noreward = models.CharField(max_length = 32)


