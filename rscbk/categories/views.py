from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import AdditemForm

@login_required
def additems(request):
    addform = AdditemForm()
    if request.method == 'POST':
        addform = AdditemForm(request.POST,request.FILES)
        if addform.is_valid():
            print(addform)
            form = addform.save(commit=False)
            form.itemuser = request.user
            form.save()
            return redirect('myuserdashboard')

    return render(request, 'additems.html', {'addform':addform})