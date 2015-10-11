#!/usr/bin/python
# -*- coding: utf-8 -*-

# coding=utf-8

#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from information.models import Info
import MySQLdb
import json
 
def mobile(request):
	return render_to_response('mobile_test.html')

def sannong(request):
	return render_to_response('form.html')

def sannong_info(request):
	return render_to_response('info.html')
	
def sixone(request):
	db = MySQLdb.connect(user='root', db='wangsong', passwd='Gab821211', host='localhost',charset='utf8')
	cursor = db.cursor()
	cursor.execute('SELECT student_id FROM information_info WHERE id=162')
	for row in cursor.fetchall():
		a = row[0]
		title = a
		a = int(a)+1
		p = Info.objects.get(name='test')
		p.student_id = a
		p.save()
	db.close()
	return render_to_response('index.html',{'title':title})

def sannong_submit(request):
	name = request.GET['name']
	class_id = request.GET['class_id']
	address = request.GET['address']
	people = request.GET['people']
	student_id = request.GET['student_id']
	phone = request.GET['phone']
	email = request.GET['email']
	birth_place = request.GET['birth_place']
	hobby = request.GET['hobby']
	project = request.GET['project']
	is_adjusted = request.GET['is_adjusted']
	interview_time = request.GET['interview_time']
	advantages = request.GET['advantages']
	gains = request.GET['gains']
	hope = request.GET['hope']
	p1 =Info(name=name,class_id=class_id,address=address,people=people,student_id=student_id,phone=phone,email=email,birth_place=birth_place,hobby=hobby,project=project,is_adjusted=is_adjusted,interview_time=interview_time,advantages=advantages,gains=gains,hope=hope)
	p1.save()
	return render_to_response('success.html')

def hellostock(request):
	db = MySQLdb.connect(user='root', db='wangsong', passwd='Gab821211', host='localhost',charset='utf8')
	cursor = db.cursor()
	cursor.execute('SELECT student_id FROM information_info WHERE id=162')
	for row in cursor.fetchall():
		p = Info.objects.get(name='test')
		p.student_id = 0
		p.save()
	db.close()
	return render_to_response("hellostock.html");

def hellostock_iframe(request,param1,param2,param3,param4,param5):
	return render_to_response("hellostock_iframe.html",{"p1":param1,"p2":param2,"p3":param3,"p4":param4,"p5":param5});

def hellostock_info(request,param1,param2,param3,param4,param5):
	if(param5=='1'):
		db = MySQLdb.connect(user='root', db='wangsong', passwd='Gab821211', host='localhost',charset='utf8')
		cursor = db.cursor()
		cursor.execute('SELECT student_id FROM information_info WHERE id=162')
		for row in cursor.fetchall():
			p = Info.objects.get(name='test')
			p.student_id = 1
			p.save()
		db.close()
	return render_to_response("hellostock_info.html",{"p1":param1,"p2":param2,"price_expect_up":param3,"price_expect_down":param4,"flag":param5});

def hellostock_mysql(request):
	db = MySQLdb.connect(user='root', db='wangsong', passwd='Gab821211', host='localhost',charset='utf8')
	cursor = db.cursor()
	cursor.execute('SELECT student_id FROM information_info WHERE id=162')
	for row in cursor.fetchall():
		a = row[0]
	db.close()
	return HttpResponse(json.dumps(a), content_type='application/json')

def saolei(request):
	return render_to_response("saolei.html")

def calculator(request,num):
	return render_to_response("calculator.html",{"stock_id":num})

def timer(request):
	return render_to_response("timer.html")

def birth(request):
	return render_to_response("birth.html")

def home(request):
	return render_to_response("home.html")