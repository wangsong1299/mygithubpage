from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import sannong,sannong_submit,sannong_info,sixone,mobile,birth
from views import hellostock,hellostock_info,hellostock_iframe,hellostock_mysql,saolei,calculator,timer
from views import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yixiu.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^work/', include('work.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sannong_submit/', sannong_submit),
    url(r'^sannong_info/', sannong_info),
    url(r'^sannong/', sannong),
	url(r'^sixone/', sixone),
	url(r'^mobile/', mobile),
	url(r'^hellostock/', hellostock),
	url(r'^hellostock_mysql/', hellostock_mysql),
	url(r'^hellostock_iframe/(\w{2})/(\d{4,6})/(\d{2,10})/(\d{2,10})/(\d{1})/', hellostock_iframe),
	url(r'^hellostock_info/(\w{2})/(\d{4,6})/(\d{2,10})/(\d{2,10})/(\d{1})/', hellostock_info),
    url(r'^saolei/', saolei),
    url(r'^calculator/(\d{0,6})', calculator),
    url(r'^timer/', timer),
    url(r'^birth/', birth),

    url(r'^$', home),


)
