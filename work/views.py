#!/usr/bin/python
# -*- coding: utf-8 -*-

#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import Text
import json
 
def index(request):
	textArr = Text.objects.all().order_by('-create_time')[:3]
	text1={}
	text2={}
	text3={}
	text1[0]=textArr[0].id
	text1[1]=textArr[0].title
	text1[2]=textArr[0].abstract
	text1[3]=textArr[0].tag
	#text1[3]=textArr[0].create_time
	text2[0]=textArr[1].id
	text2[1]=textArr[1].title
	text2[2]=textArr[1].abstract
	text2[3]=textArr[1].tag
	#text2[3]=textArr[1].create_time
	text3[0]=textArr[2].id
	text3[1]=textArr[2].title
	text3[2]=textArr[2].abstract
	text3[3]=textArr[2].tag
	return render_to_response('work.html',{'text1':json.dumps(text1),'text2':json.dumps(text2),'text3':json.dumps(text3)})

def article(request,id):
	text = Text.objects.filter(id=id)[0]
	text_title=text.title
	text_content=text.content
	text_tag = text.tag
	text_time = str(text.create_time.strftime('%Y-%m-%d %H:%M'))
	return render_to_response('work_article.html',{'text_title':json.dumps(text_title),'text_content':json.dumps(text_content),'text_tag':json.dumps(text_tag),"text_time":text.create_time})






