# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import *

from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {}
    return render(request,'home.html',context)

@login_required
def dashboard(request):
    return render(request,'dashboard.html')
