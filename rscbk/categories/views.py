from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from .forms import AdditemForm, AddbrandForm, AddcatbrandForm
from categories.models import *
from ipware.ip import get_ip
from django.db.models import Count
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib.auth.models import User

def forget_password_reset(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('pass')
        users=User.objects.get(id=user_id)
        users.set_password(password)
        users.save()
        return render(request, 'forget_password_done.html', {})


def forget_password(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        import random

        otp = "{}".format(random.randint(1000,9000))
        try:
            user = User.objects.get(username=name)
            if user:
                send_mail('Password reset verification code ', otp,
                'just2deepu@gmail.com', [user.email],fail_silently=False)
            return render(request, 'forget_password_success.html', {'otp':otp,'user_id':user.id})
        except Exception as e:
            return render(request, 'forget_password.html', {'error':e})
    return render(request, 'forget_password.html', {})


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



from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
@login_required
def delete_item(request, item_id):
    item_to_delete = Items.objects.get(id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect(reverse('myuserdashboard'))


from home.models import *

@login_required
def view_item(request, item_id):

    localip = get_ip(request)

    zero_value_items = Items.objects.filter(price=0)
    import collections
    li = []
    for i in zero_value_items:
        li.append(i.category.category_name)
    counter=collections.Counter(li)

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
      #tu = UserFullProfile.objects.get(pk=fname.id)
      t = User.objects.get(username=request.user)
      mob = ''
    except:
      pass

    context = {'free_items':sorted(counter.items()),'obj':itm_obj, 'mob':mob, 'userpro':t,'fname':fname,'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price}
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
        #up = User.objects.get(username=request.user)
    except:
        up = ''
        pass
    itm_obj = Items.objects.get(id=item_id)
    useritem  = itm_obj.itemuser
    mob = 'need to update'
    fname = User.objects.get(username=useritem)
    t = {}
    t = User.objects.get(username=useritem)
    try:
        nt = UserFullProfile.objects.get(user__username=t.username)
    except:
        nt=''
        pass

    mob = ''


    context = {'obj':itm_obj, 'mob':nt, 'userpro':t,'fname':fname,'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price}
    return render(request, 'item_details_global.html', context)


from django import forms
class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        exclude = ('itemuser','years_used',)

@login_required
def edit_item(request, pk):

    localip = get_ip(request)
    zero_value_items = Items.objects.filter(price=0)
    import collections
    li = []
    for i in zero_value_items:
        li.append(i.category.category_name)
    counter=collections.Counter(li)
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
    form = ItemForm(request.POST or None,request.FILES or None, instance=subject)
    context= { 'free_items':sorted(counter.items()), 'form':form ,'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price}

    if request.method == 'POST':
        if form.is_valid():

            form.save()
            return redirect('myuserdashboard')
    return render(request,template,context)

