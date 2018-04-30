from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from .forms import AdditemForm, AddbrandForm, AddcatbrandForm
from categories.models import *
from ipware.ip import get_ip
from django.db.models import Count
from django.core.paginator import Paginator

@login_required
def additems(request):
    localip = get_ip(request)

    itemcount = Items.objects.values('category').annotate(cate=Count('category'))
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
    addform = AdditemForm()
    cat_brd = CatBrand.objects.all()
    if request.method == 'POST':
        addform = AdditemForm(request.POST,request.FILES)
        if addform.is_valid():
            form = addform.save(commit=False)
            form.itemuser = request.user
            form.save()
            return redirect('myuserdashboard')

    return render(request, 'additems.html', {'addform':addform,'cat_brd':cat_brd,'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price})


@login_required
def addcatbrand(request):
    localip = get_ip(request)

    itemcount = Items.objects.values('category').annotate(cate=Count('category'))
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
    addform = AddcatbrandForm()
    if request.method == 'POST':
        addform = AddcatbrandForm(request.POST,request.FILES)
        if addform.is_valid():
            form = addform.save(commit=False)
            #form.itemuser = request.user
            form.save()
            return redirect('additems')

    return render(request, 'addcatbrand.html', {'addform':addform, 'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price})

@login_required
def addbrand(request):
    localip = get_ip(request)

    itemcount = Items.objects.values('category').annotate(cate=Count('category'))
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
    addform = AddbrandForm()
    if request.method == 'POST':
        addform = AddbrandForm(request.POST,request.FILES)
        if addform.is_valid():
            form = addform.save(commit=False)
            #form.itemuser = request.user
            form.save()
            return redirect('addcatbrand')

    return render(request, 'addbrand.html', {'addform':addform,'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price})









from home.models import *

@login_required
def view_item(request, item_id):

    localip = get_ip(request)

    itemcount = Items.objects.values('category').annotate(cate=Count('category'))
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
    itm_obj = Items.objects.get(id=item_id)
    useritem  = itm_obj.itemuser
    mob = 'need to update'
    fname = User.objects.get(username=useritem)
    t = {}
    try:
      t = UserFullProfile.objects.get(user=fname.id)
      mob = t.mobile
    except:
      pass

    context = {'obj':itm_obj, 'mob':mob, 'userpro':t,'fname':fname,'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price}
    return render(request, 'item_details.html', context)


@login_required
def view_item_global(request, item_id):

    localip = get_ip(request)

    itemcount = Items.objects.values('category').annotate(cate=Count('category'))
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
    itm_obj = Items.objects.get(id=item_id)
    useritem  = itm_obj.itemuser
    mob = 'need to update'
    fname = User.objects.get(username=useritem)
    t = {}
    try:
      t = UserFullProfile.objects.get(user=fname.id)
      mob = t.mobile
    except:
      pass

    context = {'obj':itm_obj, 'mob':mob, 'userpro':t,'fname':fname,'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price}
    return render(request, 'item_details_global.html', context)


from django import forms
class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        exclude = ('itemuser','years_used',)

@login_required
def edit_item(request, pk):

    localip = get_ip(request)

    itemcount = Items.objects.values('category').annotate(cate=Count('category'))
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

    subject = Items.objects.get(pk=pk)
    template = 'itemedit.html'
    form = ItemForm(request.POST or None, instance=subject)
    context= { 'form':form ,'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price}

    if request.method == 'POST':
        if form.is_valid():

            form.save()
            return redirect('myuserdashboard')
    return render(request,template,context)

