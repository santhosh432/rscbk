from django.shortcuts import render

# Create your views here.
from .forms import AdditemForm
def additems(request):
    addform = AdditemForm()

    return render(request, 'additems.html', {'addform':addform})