#!/usr/bin/python
# -*- coding: utf-8 -*-

#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import Text
import json
 
def index(request):
	return HttpResponse(1)
	
