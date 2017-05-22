# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response




from . import models
from models import *

from django.shortcuts import render
from django.template import Context,RequestContext

# Create your views here.
def welcome(request):
    data_model = Blog.objects.all()
    #print data_model
    #for i in data_model:
        #print  i.title
    return render_to_response("index.html",{'data':data_model})


def my_page(request):

    data_model = "helllooooooooo"
    if request.method == "POST":
        form_data = request.POST
        print form_data
        data_update = Blog(author=form_data['author'], title=form_data['title'],description=form_data['description'])
        data_update.save()
    #print data_model
    #for i in data_model:
        #print  i.title
    #return render_to_response('mypage.html',{'data':data_model},context=RequestContext(request))
    context = {'data':data_model}
    return render(request,'mypage.html',context)
