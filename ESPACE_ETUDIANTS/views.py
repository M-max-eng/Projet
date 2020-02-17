# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'login.html')

def toregister(request):
    return render(request,'register.html')

def pwd(request):
    return render(request,'forgot-password.html')

def index(request):
    return render(request,'blank.html')