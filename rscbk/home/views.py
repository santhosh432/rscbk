# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from categories.models import Category,Items
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from home.models import UserFullProfile
from ipware.ip import get_ip
from .forms import *
from home.models import Feedback

# Create your views here.
def dash_help(request):

    context = {}

    return render(request,'dashboard_help.html',context)

# Create your views here.
def aboutus(request):
    localip = get_ip(request)

    context = {'localip':localip}

    return render(request,'aboutus.html',context)

# Create your views here.
def contactus(request):
    localip = get_ip(request)

    context = {'localip':localip}

    return render(request,'contactus.html',context)


def feedback(request):
    fback = Feedback.objects.all().order_by('-id')[:5]
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form,'fback':fback})


# Create your views here.
def terms(request):
    localip = get_ip(request)

    context = {'localip':localip}
    return render(request,'terms.html',context)

# Create your views here.
def privacy(request):
    localip = get_ip(request)

    context = {'localip':localip}
    return render(request,'privacy.html',context)

def home(request):
    localip = get_ip(request)

    context = {'localip':localip}
    return render(request,'main.html',context)
from home.models import Feedback
# Create your views here.
def base(request):
    localip = get_ip(request)
    fback = Feedback.objects.all()
    context = {'localip':localip, 'fback':fback}
    return render(request,'base.html',context)

def homepage(request):
    localip = get_ip(request)
    fback = Feedback.objects.all()
    context = {'localip':localip, 'fback':fback}

    return render(request,'home.html',context)

@login_required
def myuserdashboard(request):
    localip = get_ip(request)


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
    try:
        up = UserFullProfile.objects.get(user=request.user)
    except:
        up = ''
        pass


    return render(request, 'userdashboard.html',{'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price})
from django.core.paginator import Paginator

@login_required
def myuserdashboard_with_cat(request,cat_id=None):
    localip = get_ip(request)
    cat = Category.objects.all()
    items_cat = Items.objects.filter(category__id=cat_id).exclude(itemuser=request.user)


    items_cat_max = Items.objects.filter(category__id=cat_id).exclude(itemuser=request.user).order_by('-price').first()
    items_cat_min = Items.objects.filter(category__id=cat_id).exclude(itemuser=request.user).order_by('-price').last()

    brand_dict = {}
    for i in items_cat:
        brand_dict[i.bnd.id] = i.bnd.brand_name

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
    select_value = 0
    return render(request, 'userdashboard.html',{'localip':localip,'items_cat_min':items_cat_min,'items_cat_max':items_cat_max,'brand_dict_all':brand_dict,'select_value':select_value,'brand_dict':brand_dict,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'useritemscount_cat':useritemscount_cat,'totcount_cat':totcount_cat,'heading':heading,'items_cat':items_cat})


@login_required
def myuserdashboard_with_cat_bnd(request,cat_id=None,bnd_id=None):
    localip = get_ip(request)
    cat = Category.objects.all()
    items_cat_all = Items.objects.filter(category__id=cat_id).exclude(itemuser=request.user)
    items_cat = Items.objects.filter(category__id=cat_id,bnd__id=bnd_id).exclude(itemuser=request.user)
    items_cat_max = Items.objects.filter(category__id=cat_id,bnd__id=bnd_id).exclude(itemuser=request.user).order_by('-price').first()
    items_cat_min = Items.objects.filter(category__id=cat_id,bnd__id=bnd_id).exclude(itemuser=request.user).order_by('-price').last()

    brand_dict_all = {}
    brand_dict = {}
    for i in items_cat_all:
        brand_dict_all[i.bnd.id] = i.bnd.brand_name
    for i in items_cat:
        brand_dict[i.bnd.id] = i.bnd.brand_name

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

    select_value = bnd_id
    return render(request, 'userdashboard.html',{'localip':localip,'items_cat_min':items_cat_min,'items_cat_max':items_cat_max,'select_value':select_value,'brand_dict':brand_dict,'brand_dict_all':brand_dict_all,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'useritemscount_cat':useritemscount_cat,'totcount_cat':totcount_cat,'heading':heading,'items_cat':items_cat})


@login_required
def myuserdashboard_with_cat_bnd_min_max(request,cat_id=None,bnd_id=None,min_id=None, max_id=None):
    localip = get_ip(request)
    cat = Category.objects.all()
    items_cat_all = Items.objects.filter(category__id=cat_id).exclude(itemuser=request.user)
    items_cat = Items.objects.filter(category__id=cat_id,bnd__id=bnd_id,price__range=(min_id, max_id)).exclude(itemuser=request.user)
    items_cat_max = Items.objects.filter(category__id=cat_id,bnd__id=bnd_id,price__range=(min_id, max_id)).exclude(itemuser=request.user).order_by('-price').first()
    items_cat_min = Items.objects.filter(category__id=cat_id,bnd__id=bnd_id,price__range=(min_id, max_id)).exclude(itemuser=request.user).order_by('-price').last()

    brand_dict_all = {}
    brand_dict = {}
    for i in items_cat_all:
        brand_dict_all[i.bnd.id] = i.bnd.brand_name
    for i in items_cat:
        brand_dict[i.bnd.id] = i.bnd.brand_name

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

    select_value = bnd_id
    return render(request, 'userdashboard.html',{'localip':localip,'items_cat_min':items_cat_min,'items_cat_max':items_cat_max,'select_value':select_value,'brand_dict':brand_dict,'brand_dict_all':brand_dict_all,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'useritemscount_cat':useritemscount_cat,'totcount_cat':totcount_cat,'heading':heading,'items_cat':items_cat})




def dashboard(request):
    return render(request,'dashboard.html')

def sign_up(request):
        localip = get_ip(request)
        context={'localip':localip}
        if request.method == 'POST':
            if "s_username" in request.POST and 's_pass' in request.POST and 's_passr' in request.POST and 'email' in request.POST:
                username = request.POST.get('s_username')
                password = request.POST.get('s_pass')
                passwordr = request.POST.get('s_passr')
                email = request.POST.get('email')
                first_name = request.POST.get('s_fullname')
                mobile = request.POST.get('s_mobile')
                if password == passwordr:
                    try:
                        u = User.objects.create_user(username, email, password)
                        u.first_name = first_name
                        up = UserFullProfile(user=u, mobile=mobile)
                        up.save()
                        u.save()

                        print('userprofile.............')
                        print(up.mobile)
                        return HttpResponseRedirect(reverse('/login'))
                    except:
                        pass #
            return render(request, 'sucess.html', context)
        else:
            return render(request, 'signup.html', context)

