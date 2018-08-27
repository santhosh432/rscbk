from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from .forms import AdditemForm, AddbrandForm, AddcatbrandForm, AddwishlistForm
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
                'support@redsuncube.com', [user.email],fail_silently=False)
            return render(request, 'forget_password_success.html', {'otp':otp,'user_id':user.id})
        except Exception as e:

            #user = User.objects.get(username=name)
            #if user:
            #    send_mail('Password reset verification code ', otp,
            #    'support@redsuncube.com', [user.email],fail_silently=False)
            #return render(request, 'forget_password_success.html', {'otp':otp,'user_id':user.id})


            return render(request, 'forget_password.html', {'error':e})

    return render(request, 'forget_password.html', {})
from ipware.ip import get_ip
@login_required
def addwishlist(request):
    form = AddwishlistForm
    localip = get_ip(request)
    global_wishlist = Wishlist.objects.all().exclude(wishlist_user=request.user.id)
    if request.method == 'POST':
        addform = AddwishlistForm(request.POST,request.FILES)
        if addform.is_valid():
            form = addform.save(commit=False)
            form.wishlist_user = request.user
            form.save()
            user_wishlist = Wishlist.objects.filter(wishlist_user=request.user.id)
            localip = get_ip(request)

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

    return render(request, 'add_wishlist.html', {'form':form,'localip':localip,'global_wishlist':global_wishlist})



@login_required
def additems(request):
    localip = get_ip(request)

    itemcount = Items.objects.values('category').annotate(cate=Count('category'))
    cat = Category.objects.all().exclude(status=False)
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
from home.models import *

@login_required
def addcatbrand(request,cat_id):
    localip = get_ip(request)

    itemcount = Items.objects.values('category').annotate(cate=Count('category'))
    cat = Category.objects.all().exclude(status=False)
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
        bd_name = request.POST.get('bnd_name')
        ct = request.POST.get('cat_nam')
        c_obj = Category.objects.get(id=ct)

        n = Brand.objects.create(brand_name=bd_name)
        n.save()
        m = CatBrand.objects.create(cat_nam=c_obj,bnd_name=n)
        m.save()

        return redirect('additems')

    return render(request, 'addcatbrand.html', {'cat_id':cat_id,'addform':addform, 'itemc':itemcount,'localip':localip,'up':up,'allcat':cat,'items':items,'useritemscount':useritemscount,'totcount':totcount,'heading':heading,'global_items_count':global_items_count,'global_items_price':global_items_price})







@login_required
def addbrand(request):
    localip = get_ip(request)

    itemcount = Items.objects.values('category').annotate(cate=Count('category'))
    cat = Category.objects.all().exclude(status=False)
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
    cat = Category.objects.all().exclude(status=False)
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
    cat = Category.objects.all().exclude(status=False)
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
    item_image = forms.ImageField(label='Image 1',required=False, widget=forms.FileInput)
    item_image2 = forms.ImageField(label='Image 1',required=False, widget=forms.FileInput)

    class Meta:
        model = Items
        exclude = ('itemuser','years_used',)

    def __init__(self, *args, **kwargs):
        self.category = Category.objects.exclude(category_name='Cash')
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = self.category

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
    cat = Category.objects.all().exclude(status=False)
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

# ====================== UDB ===========================

def udb_add_item(request):
    addform = AdditemForm()

    context = {'addform': addform}
    return render(request, 'categories/add_item.html' , context)

# left
def cat_details(request):
    try:
        del request.session['tonehome']
    except KeyError:
        pass

    request.session['tonecatdet'] = True
    context= {}

    return render(request, 'home/udb_home.html' , context)

