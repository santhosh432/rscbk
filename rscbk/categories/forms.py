from django.forms import ModelForm
from django import forms
from .models import Category,Items


class AdditemForm(forms.ModelForm):
    # model = Category
    class Meta:
        model = Items
        exclude = ('',)
