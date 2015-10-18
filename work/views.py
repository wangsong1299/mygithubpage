#!/usr/bin/python
# -*- coding: utf-8 -*-

#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from work.models import Text
import json
 
def index(request):
	textArr = Text.objects.all().order_by('-create_time')[:5]
	text1={}
	text2={}
	text3={}
	text4={}
	text5={}
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
	text4[0]=textArr[3].id
	text4[1]=textArr[3].title
	text4[2]=textArr[3].abstract
	text4[3]=textArr[3].tag
	text5[0]=textArr[4].id
	text5[1]=textArr[4].title
	text5[2]=textArr[4].abstract
	text5[3]=textArr[4].tag
	return render_to_response('work.html',{'text1':json.dumps(text1),'text2':json.dumps(text2),'text3':json.dumps(text3),'text4':json.dumps(text4),'text5':json.dumps(text5)})

def article(request,id):
	text = Text.objects.filter(id=id)[0]
	text_title=text.title
	text_content=text.content
	text_tag = text.tag
	text_time = str(text.create_time.strftime('%Y-%m-%d %H:%M'))
	return render_to_response('work_article.html',{'text_title':json.dumps(text_title),'text_content':json.dumps(text_content),'text_tag':json.dumps(text_tag),"text_time":text.create_time})






