from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from .forms import AdditemForm, AddbrandForm
from categories.models import *

@login_required
def additems(request):
    addform = AdditemForm()
    if request.method == 'POST':
        addform = AdditemForm(request.POST,request.FILES)
        if addform.is_valid():
            form = addform.save(commit=False)
            form.itemuser = request.user
            form.save()
            return redirect('myuserdashboard')

    return render(request, 'additems.html', {'addform':addform})


@login_required
def addbrand(request):
    addform = AddbrandForm()
    if request.method == 'POST':
        addform = AddbrandForm(request.POST,request.FILES)
        if addform.is_valid():
            form = addform.save(commit=False)
            #form.itemuser = request.user
            form.save()
            return redirect('additems')

    return render(request, 'addbrand.html', {'addform':addform})
from home.models import *

@login_required
def view_item(request, item_id):
    itm_obj = Items.objects.get(id=item_id)
    mob = 'need to update'
    fname = User.objects.get(username=request.user)
    t = {}
    try:
      t = UserFullProfile.objects.get(user=request.user.id)
      mob = t.mobile
    except:
      pass

    context = {'obj':itm_obj, 'mob':mob, 'userpro':t,'fname':fname}
    return render(request, 'item_details.html', context)