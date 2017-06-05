from django.conf.urls import url,include
from django.contrib import admin
from sadhanaApp import views
urlpatterns = [
    url(r'^$', views.my_page),
    url(r'^data/$', views.welcome),
    url(r'^mybiography/$',views.my_info),
    url(r'^datafile/$',views.my_info)
    #url(r'^myInfo/$', views.my_info)
    #url(r'^myInfo/',views.my_page)
]
