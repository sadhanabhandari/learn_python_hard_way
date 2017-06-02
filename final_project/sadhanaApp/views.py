# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from models import UserInfo
from django.template import Context,RequestContext

# Create your views here.


def my_page(request):

    data_model = "Sadhana's page"
    if request.method == "POST":
        form_data = request.POST
        print form_data
        data_update = UserInfo(firstName=form_data['firstName'], lastName=form_data['lastName'],address=form_data['address'],email=form_data['email'],phoneNumber=form_data['phoneNumber'])
        data_update.save()
    context = {'data':data_model}
    return render(request,'index.html',context)

def welcome(request):
    data_model=UserInfo.objects.all()
    context={'data':data_model}
    #return render_to_response('datafile.html',{'data':data_model})
    return render(request,'datafile.html',context)

def my_info(request):
    data_model = "helllooooooooo"
    if request.method == "POST":
        form_data = request.POST
        print form_data
        data_update = UserInfo(firstName=form_data['firstName'], lastName=form_data['lastName'],address=form_data['address'],email=form_data['email'],phoneNumber=form_data['phoneNumber'])
        print "hellooo"
        data_update.save()
    context = {'data':data_model}
    return render(request,'mybiography.html',context)