# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import *
from categories.models import Category,Items
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
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
    useritemscount = items.count()
    totcount = sum([tot.price for tot in items])
    heading = "My"
    return render(request, 'userdashboard.html',{'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading})

def myuserdashboard_with_cat(request,cat_id=None):
    cat = Category.objects.all()
    items_cat = Items.objects.filter(category__id=cat_id)
    items = Items.objects.filter(itemuser=request.user)
    useritemscount = items.count()
    totcount = sum([tot.price for tot in items])
    useritemscount_cat = items_cat.count()
    totcount_cat = sum([tot.price for tot in items_cat])

    heading = "All"
    return render(request, 'userdashboard.html',{'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'useritemscount_cat':useritemscount_cat,'totcount_cat':totcount_cat,'heading':heading,'items_cat':items_cat})


# @login_required
def dashboard(request):
    return render(request,'dashboard.html')

def sign_up(request):
        users = User.objects.all()
        context={}
        if request.method == 'POST':
                # sign-up
                if "s_username" in request.POST and 's_pass' in request.POST and 's_passr' in request.POST and 'email' in request.POST:
                        username = request.POST.get('s_username')
                        password = request.POST.get('s_pass')
                        passwordr = request.POST.get('s_passr')
                        email = request.POST.get('email')

                        if password == passwordr:
                                try:
                                        User.objects.create_user(username, email, password)
                                        user = authenticate(username=username, password=password)
                                        login(request, user)
                                        return HttpResponseRedirect(reverse('home'))
                                except:
                                        error_info="Error, please check inputs..."
                                        #ireturn render_to_response('sign_up.html', locals(), context_instance=RequestContext(request))
                                        return render(request, 'signup.html', context)
        #ireturn render_to_response('sign_up.html',  context_instance=RequestContext(request))
        return render(request, 'signup.html', context)

