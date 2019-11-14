# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.template import loader
import datetime
from django.http import HttpResponse

from phoenix.forms import EmpForm

def homepage(request):
    #now = datetime.datetime.now()
    template = loader.get_template('homepage.html')
    name = {
        'emp_name':'microfocus'
    }
    return HttpResponse(template.render(name))

def index(request):
    Emp = EmpForm()
    return render(request,"index.html",{'forms':Emp})