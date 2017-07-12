# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from . import models

# Create your views here.

# def today(request):
#     

def index(request):
    context = {
    "date":"today"
    }
    return render(request,'first_app/index.html', context)



def a_view(request):
    return render_to_response("a_template.html", {
        'time':datetime.now(),
        }, context_instance=RequestContext(request))


    

time = datetime.now()

