from django.conf.urls import patterns, include, url
from work import views


urlpatterns = patterns('',
     
    url(r'^$', views.index),   
    url(r'^article/(\d{1,4})/$', views.article),   
)
