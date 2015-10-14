#!/usr/bin/python
# -*- coding: utf-8 -*-

#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import Text
import json
 
def index(request):
	textArr = Text.objects.all().order_by('-create_time')[:2]
	text1={}
	text2={}
	text1[0]=textArr[0].title
	text1[1]=textArr[0].content
	text1[2]=textArr[0].tag
	#text1[3]=textArr[0].create_time
	text2[0]=textArr[1].title
	text2[1]=textArr[1].content
	text2[2]=textArr[1].tag
	#text2[3]=textArr[1].create_time
	return render_to_response('blog.html',{'text1':json.dumps(text1),'text2':json.dumps(text2)})
