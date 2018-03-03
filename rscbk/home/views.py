# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import *
from categories.models import Category,Items
from django.shortcuts import render

def home(request):
    context = {}
    return render(request,'main.html',context)

# Create your views here.
def homepage(request):

    context = {}
    return render(request,'home.html',context)

@login_required
def myuserdashboard(request):
    cat = Category.objects.all()
    items = Items.objects.filter(itemuser=request.user)
    print(items.count())
    useritemscount = items.count()
    print(sum([tot.price for tot in items]))
    totcount = sum([tot.price for tot in items])

    print('ok')
    return render(request, 'userdashboard.html',{'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount})


# @login_required
def dashboard(request):
    return render(request,'dashboard.html')


