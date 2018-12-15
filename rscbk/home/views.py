# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from categories.models import Wishlist, Items, CatBrand, Category, Userwhishlist, UserViewedItems, RequestedItems
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from home.models import UserFullProfile
from ipware.ip import get_ip
from .forms import *
from home.models import Feedback
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from categories.forms import AdditemForm
from django.db.models import Sum
# Create your views here.

@login_required
def wishlist(request):
    global_wishlist = Wishlist.objects.all().exclude(wishlist_user=request.user.id)
    user_wishlist = Wishlist.objects.filter(wishlist_user=request.user.id)
    localip = get_ip(request)
    usercount = User.objects.all().count()
    freeitemc = Items.objects.filter(price=0).count()
    itemcount = Items.objects.values('category').annotate(cate=Count('category')).exclude(itemuser=request.user)
    zero_value_items = Items.objects.filter(price=0)
    import collections
    li = []
    for i in zero_value_items:
        li.append(i.category.category_name)
    counter=collections.Counter(li)


    cat = Category.objects.all().exclude(status=False)
    items = Items.objects.filter(itemuser=request.user)
    useritemscount = items.count()
    totcount = sum([tot.price for tot in items])
    global_items = Items.objects.all().exclude(itemuser=request.user)
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
    ctx = {'free_items':sorted(counter.items()),'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,
           'totcount':totcount,'heading':heading,'global_items_count':global_items_count,
           'global_items_price':global_items_price,'localip':localip,'u':usercount,'fc':freeitemc,'user_wishlist':user_wishlist,'global_wishlist':global_wishlist}





    return render(request,'wishlist.html',ctx)


# Create your views here.
def main_home(request):
    localip = get_ip(request)
    items_obj = Items.objects.all().order_by('-id')[:9]
    context = {'items_obj':items_obj, 'localip':localip}

    return render(request,'main_home.html',context)

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
            form.customer_name = request.user
            form.save()
            return render(request, 'thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form,'fback':fback})




from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
@login_required

def change_password(request):

    form = ChangePasswordForm(request.POST)
    new_password = "0"
    confirm_password = "0"
    if request.method =='POST':
        user = User.objects.get(id=request.user.id)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            try:


                if new_password == confirm_password:
                    user_check = authenticate(request, username=request.user.username, password=old_password)
                    print (user_check,"user_hcheck")
                    if user_check is not None:
                        user.set_password(new_password)
                        user.save()
                        localip = get_ip(request)
                        usercount = User.objects.all().count()
                        freeitemc = Items.objects.filter(price=0).count()
                        itemcount = Items.objects.values('category').annotate(cate=Count('category')).exclude(itemuser=request.user)
                        zero_value_items = Items.objects.filter(price=0)
                        import collections
                        li = []
                        for i in zero_value_items:
                            li.append(i.category.category_name)
                        counter=collections.Counter(li)


                        cat = Category.objects.all().exclude(status=False)
                        items = Items.objects.filter(itemuser=request.user)
                        useritemscount = items.count()
                        totcount = sum([tot.price for tot in items])
                        global_items = Items.objects.all().exclude(itemuser=request.user)
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
                        ctx = {'free_items':sorted(counter.items()),'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,
                               'totcount':totcount,'heading':heading,'global_items_count':global_items_count,
                               'global_items_price':global_items_price,'localip':localip,'u':usercount,'fc':freeitemc}

                        return render(request, 'userdashboard.html',ctx)







                        #return reverse("myuserdashboard")
                    else:
                        error = "Please Enter the correct old password"
                        context = {'form':form, 'msg':error}
                        return render(request,'change_password.html',context)
                else:

                    error = "Please ensure the new password and confirm password are same"
                    context = {'form':form, 'msg':error}
                    return render(request,'change_password.html',context)
            except Exception as e:
                pass


    context = {'form':form, 'user': request.user, 'new_pwd': new_password, 'conf_pwd': confirm_password}
    return render(request,'change_password.html',context)

import random
from random import randint
from django.db.models import Max

# Create your views here.
def welcome(request):
    localip = get_ip(request)

    try:
        max_id = Items.objects.all().aggregate(max_id=Max("id"))['max_id']
        pk = random.randint(1, max_id)
        items_randoom = Items.objects.get(pk=pk)
    except Exception:
            get_list = Items.objects.all()
            id_list = []
            for i in get_list:
                id_list.append(i.id)

            # pk = random.choice(id_list)
            # items_randoom = Items.objects.get(pk=pk)
            items_randoom = 0


    context = {'localip':localip,'useritems':items_randoom}
    return render(request,'home.html',context)


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
    localip = '67564543'

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
    localip = '67564543'

    context = {'localip':localip, 'fback':fback}

    return render(request,'home.html',context)
from django.db.models import Count

@login_required
def myuserdashboard(request):
    localip = get_ip(request)
    usercount = User.objects.all().count()
    freeitemc = Items.objects.filter(price=0).count()
    itemcount = Items.objects.values('category').annotate(cate=Count('category')).exclude(itemuser=request.user)
    zero_value_items = Items.objects.filter(price=0)
    import collections
    li = []
    for i in zero_value_items:
        li.append(i.category.category_name)
    counter=collections.Counter(li)


    cat = Category.objects.all().exclude(status=False)
    items = Items.objects.filter(itemuser=request.user)
    useritemscount = items.count()
    totcount = sum([tot.price for tot in items])
    global_items = Items.objects.all().exclude(itemuser=request.user)
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
    ctx = {'free_items':sorted(counter.items()),'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,
           'totcount':totcount,'heading':heading,'global_items_count':global_items_count,
           'global_items_price':global_items_price,'localip':localip,'u':usercount,'fc':freeitemc}

    return render(request, 'userdashboard.html',ctx)


@login_required
def myuserdashboardtest(request):
    localip = get_ip(request)
    usercount = User.objects.all().count()
    freeitemc = Items.objects.filter(price=0).count()
    itemcount = Items.objects.values('category').annotate(cate=Count('category')).exclude(itemuser=request.user)
    zero_value_items = Items.objects.filter(price=0)
    import collections
    li = []
    for i in zero_value_items:
        li.append(i.category.category_name)
    counter=collections.Counter(li)


    cat = Category.objects.all()
    items = Items.objects.filter(itemuser=request.user)
    useritemscount = items.count()
    totcount = sum([tot.price for tot in items])
    global_items = Items.objects.all().exclude(itemuser=request.user)
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
    ctx = {'free_items':sorted(counter.items()),'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,
           'totcount':totcount,'heading':heading,'global_items_count':global_items_count,
           'global_items_price':global_items_price,'localip':localip,'u':usercount,'fc':freeitemc}

    return render(request, 'userdashboardtest.html',ctx)




from django.core.paginator import Paginator

@login_required
def myuserdashboard_with_cat(request,cat_id=None):
    localip = get_ip(request)
    cat = Category.objects.all().exclude(status=False)
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
def myuserdashboard_with_cat_freelist(request,cat_id=None):
    localip = get_ip(request)
    cat = Category.objects.all().exclude(status=False)
    items_cat = Items.objects.filter(category__id=cat_id,price=0).exclude(itemuser=request.user)


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
    cat = Category.objects.all().exclude(status=False)
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
    cat = Category.objects.all().exclude(status=False)
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



from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from home.forms import SignUpForm
def sign_up(request):
    context={}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            nuser = User.objects.get(username=form.cleaned_data.get('username'))
            ufp = UserFullProfile(user=nuser,mobile=form.cleaned_data.get('mobile'))
            ufp.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #login(request)
            return render(request, 'sucess.html', context)
            #return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


from django.contrib.auth import (login as auth_login,  authenticate)
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def login(request):
    localip = get_ip(request)
    _message = 'Please sign in'
    img_obj1 = Items.objects.all().order_by('-id')[:6]
    img_obj2 = Items.objects.all().order_by('-id')[7:12]
    img_obj3 = Items.objects.all().order_by('-id')[13:18]
    context = {'message': _message,'localip':localip,'img_obj1':img_obj1,'img_obj2':img_obj2,'img_obj3':img_obj3,}
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                localip = get_ip(request)
                usercount = User.objects.all().count()
                freeitemc = Items.objects.filter(price=0).count()
                itemcount = Items.objects.values('category').annotate(cate=Count('category')).exclude(itemuser=request.user)
                zero_value_items = Items.objects.filter(price=0)
                import collections
                li = []
                for i in zero_value_items:
                    li.append(i.category.category_name)
                counter=collections.Counter(li)


                cat = Category.objects.all().exclude(status=False)
                items = Items.objects.filter(itemuser=request.user)
                useritemscount = items.count()
                totcount = sum([tot.price for tot in items])
                global_items = Items.objects.all().exclude(itemuser=request.user)
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
                ctx = {'free_items':sorted(counter.items()),'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,
                       'totcount':totcount,'heading':heading,'global_items_count':global_items_count,
                       'global_items_price':global_items_price,'localip':localip,'u':usercount,'fc':freeitemc}

                return render(request, 'userdashboard.html',ctx)







            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'

    return render(request, 'main_home.html', context)






from django.views.generic import FormView

class NewUserProfileView(FormView):
    template_name = "user_profile.html"
    form_class = UserProfileForm

    def form_valid(self, form):
        form.save(self.request.user)
        return super(NewUserProfileView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("some url name")





from django.views.generic import UpdateView

class EditUserProfileView(UpdateView):
    #Note that we are using UpdateView and not FormView
    model = UserFullProfile
    form_class = UserProfileForm
    template_name = "user_profile.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return user.userfullprofile

    def get_success_url(self, *args, **kwargs):
        return reverse("myuserdashboard")
# ========================================= new UDB ===============

def delallsessions(request, ses):
    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass

@login_required
def my_items(request):
    localip = get_ip(request)

    myuser = UserFullProfile.objects.get(user=request.user)

    uform = MyUserprofile(instance=myuser)
    change_form = PasswordChangeForm(request.user)
    cat_brd = CatBrand.objects.all()
    wlist = Userwhishlist.objects.filter(user=request.user)


    try:
        catidpk = request.session['catid']
    except KeyError:
        catidpk = 1
    cat = Category.objects.get(pk=catidpk)
    all_ctx = {'all_cat': Category.objects.all(),
               'all_user_items' : Items.objects.filter(itemuser=request.user),
               'one_cat_items': Items.objects.filter(category=cat).exclude(itemuser=request.user),
               'uform': uform,
               'change_form': change_form,
               'cat_brd':cat_brd,
               'additemform':AdditemForm(),
               'wlist': wlist,
               'notification_count':Items.objects.select_related('req_myitems').filter(itemuser=request.user).count(),
               'req_items': RequestedItems.objects.select_related('citem').filter(citem__itemuser=request.user).count(),
               'item_price': Items.objects.aggregate(Sum('price')),
               'myitem_price': Items.objects.filter(itemuser=request.user).aggregate(Sum('price')),
               'total_items' : Items.objects.all().count(),
               'localip':localip}
    print(Items.objects.aggregate(Sum('price')))
    return all_ctx


@login_required
def udb_home(request):
    ses = ['ttwohome','ttwoabouts','ttwohelp','ttwonotifcations','twowhishlist', 'twoadditems','twomyprofile','twochangepwd']

    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass

    request.session['tonehome'] = True
    request.session['ttwohome'] = True

    myitems = my_items(request)

    context = myitems
    # print(context)
    return render(request, 'home/udb_home.html', context)


# right
@login_required
def udb_righthome(request):
    ses = ['ttwohome','ttwoabouts','ttwohelp','ttwonotifcations','twowhishlist', 'twoadditems','twomyprofile','twochangepwd']

    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass

    request.session['ttwohome'] = True

    myitems = my_items(request)
    print(myitems)

    context = myitems
    return render(request, 'home/udb_home.html', context)


# right
@login_required
def udb_aboutus(request):
    #del request.session['tonehome']
    ses = ['ttwohome','ttwoabouts','ttwohelp','ttwonotifcations','twowhishlist', 'twoadditems','twomyprofile','twochangepwd']

    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass

    request.session['ttwoabouts'] = True

    myitems = my_items(request)

    context = myitems
    return render(request, 'home/udb_home.html', context)


# right
@login_required
def udb_help(request):
    ses = ['ttwohome','ttwoabouts','ttwohelp','ttwonotifcations','twowhishlist', 'twoadditems','twomyprofile','twochangepwd']

    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass

    request.session['ttwohelp'] = True
    myitems = my_items(request)

    context = myitems
    return render(request, 'home/udb_home.html', context)

# right
@login_required
def udb_notifications(request):
    ses = ['ttwohome','ttwoabouts','ttwohelp','ttwonotifcations','twowhishlist', 'twoadditems','twomyprofile','twochangepwd']
    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass

    request.session['ttwonotifcations'] = True
    myitems = my_items(request)

    context = myitems
    return render(request, 'home/udb_home.html', context)


# right
@login_required
def udb_whishlist(request):
    ses = ['ttwohome','ttwoabouts','ttwohelp','ttwonotifcations','twowhishlist', 'twoadditems','twomyprofile','twochangepwd']
    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass

    request.session['twowhishlist'] = True
    myitems = my_items(request)

    context = myitems
    return render(request, 'home/udb_home.html', context)


# right
@login_required
def udb_addmyitems(request):
    ses = ['ttwohome','ttwoabouts','ttwohelp','ttwonotifcations','twowhishlist', 'twoadditems','twomyprofile','twochangepwd']
    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass

    request.session['twoadditems'] = True

    if request.method == 'POST':
        additemform = AdditemForm(request.POST, request.FILES)
        if additemform.is_valid():
            # additemform.
            ad = additemform.save(commit=False)
            ad.itemuser = request.user
            ad.save()
            return redirect('homeapp:udb_righthome')
    else:

        additemform = AdditemForm()

    myitems = my_items(request)

    context = myitems
    context.update({'additemform': additemform})

    return render(request, 'home/udb_home.html', context)


# right
@login_required
def udb_myprofile(request, pk=1):


    # print(request.session['tonehome'])
    ses = ['ttwohome','ttwoabouts','ttwohelp','ttwonotifcations','twowhishlist', 'twoadditems','twomyprofile','twochangepwd']
    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass
    request.session['twomyprofile'] = True

    myuser = UserFullProfile.objects.get(user=request.user)

    if request.method == 'POST':
        uform = MyUserprofile(request.POST or None, request.FILES, instance=myuser)
        if uform.is_valid():
            uform.save()
            messages.success(request, 'Successfully Updated your Profile')

        return redirect('homeapp:udb_myprofile')

    uform = MyUserprofile(instance=myuser)

    myitems = my_items(request)

    context = myitems
    ctx = {'uform': uform}
    # print(context)
    # print(ctx)

    context.update(ctx)
    # print(context)

    return render(request, 'home/udb_home.html', context)

# right
@login_required
def udb_change_pwd(request):
    ses = ['ttwohome','ttwoabouts','ttwohelp','ttwonotifcations','twowhishlist', 'twoadditems','twomyprofile','twochangepwd']
    for s in ses:
        try:
            del request.session[s]
        except KeyError:
            pass
    request.session['twochangepwd'] = True

    if request.method == 'POST':
        change_form = PasswordChangeForm(request.user, request.POST)
        if change_form.is_valid():
            user = change_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        change_form = PasswordChangeForm(request.user)

    myitems = my_items(request)

    context = myitems
    context.update({'change_form': change_form})
    return render(request, 'home/udb_home.html', context)


from django.http import JsonResponse
def del_item(request):
    itemid = request.GET.get('itemid', None)

    Items.objects.filter(pk= itemid).delete()
    data = {}

    return JsonResponse(data)

from django.db import IntegrityError
def udb_addtowishlist(request):
    itemid = request.GET.get('itemid', None)
    item = Items.objects.get(pk=int(itemid))

    try:
        addwish = Userwhishlist(item=item, user=request.user)
        addwish.save()
        print('wishlist added done',itemid , item.item_name)

    except IntegrityError:
        print('inte error')
        pass

    data = {}

    return JsonResponse(data)

def udb_addto_vieweditem(request):
    itemid = request.GET.get('itemid', None)
    item = Items.objects.get(pk=int(itemid))

    vitem = UserViewedItems(vitem=item, vuser=request.user)
    vitem.save()

    data = {'vitem':vitem.vuser.username }

    return JsonResponse(data)

def udb_requested_items(request):
    myitem = request.GET.get('myitem', None)
    citem = request.GET.get('citem', None)

    myitem_obj = Items.objects.get(pk=myitem)
    citem_obj = Items.objects.get(pk=citem)

    reitem = RequestedItems(ruser= request.user, myitem= myitem_obj, citem = citem_obj)
    reitem.save()
    data = {}
    return JsonResponse(data)

from django.shortcuts import HttpResponse


def homepage(request):
    all_ctx = {'all_cat': Category.objects.all()}
    return render(request, 'home/homepage.html', all_ctx)
