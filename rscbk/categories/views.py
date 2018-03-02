from django.shortcuts import render,redirect

# Create your views here.
from .forms import AdditemForm
def additems(request):
    addform = AdditemForm()
    if request.method == 'POST':
        addform = AdditemForm(request.POST)
        if addform.is_valid():
            form = addform.save(commit=False)
            form.itemuser = request.user
            form.save()
            return redirect('myuserdashboard')

    return render(request, 'additems.html', {'addform':addform})