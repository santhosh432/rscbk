# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from categories.models import Category,Items
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

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
    global_items = Items.objects.all()
    global_items_count = global_items.count()
    global_items_price = sum([tot.price for tot in global_items])
    heading = "My"
    paginator1 = Paginator(items, 10)
    page1 = request.GET.get('page', 1)
    items = paginator1.page(page1)
    return render(request, 'userdashboard.html',{'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price})
from django.core.paginator import Paginator

@login_required
def myuserdashboard_with_cat(request,cat_id=None):
    cat = Category.objects.all()
    items_cat = Items.objects.filter(category__id=cat_id).exclude(itemuser=request.user)
    useritemscount_cat = items_cat.count()

    paginator = Paginator(items_cat, 10)
    page = request.GET.get('pagee', 1)
    items_cat = paginator.page(page)

    items = Items.objects.filter(itemuser=request.user)
    useritemscount = items.count()
    totcount = sum([tot.price for tot in items])
    totcount_cat = sum([tot.price for tot in items_cat])

    heading = "All"
    paginator1 = Paginator(items, 10)
    page1 = request.GET.get('page', 1)
    items = paginator1.page(page1)
    return render(request, 'userdashboard.html',{'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'useritemscount_cat':useritemscount_cat,'totcount_cat':totcount_cat,'heading':heading,'items_cat':items_cat})


def dashboard(request):
    return render(request,'dashboard.html')

def sign_up(request):
        context={}
        if request.method == 'POST':
            if "s_username" in request.POST and 's_pass' in request.POST and 's_passr' in request.POST and 'email' in request.POST:
                username = request.POST.get('s_username')
                password = request.POST.get('s_pass')
                passwordr = request.POST.get('s_passr')
                email = request.POST.get('email')
                if password == passwordr:
                    try:
                        User.objects.create_user(username, email, password)
                        return HttpResponseRedirect(reverse('/login'))
                    except:
                        pass #
            return render(request, 'main.html', context)
        else:
            return render(request, 'signup.html', context)

