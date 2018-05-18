#from django.forms import ModelForm
from django import forms
from .models import Items, CatBrand
from home.models import Brand


class AddbrandForm(forms.ModelForm):
    #model = Brand

    class Meta:
        model = Brand
        fields = ('brand_name',)
    #    #exclude = ('itemuser',)

class AddcatbrandForm(forms.ModelForm):
    #model = Brand

    class Meta:
        model = CatBrand
        fields = ('cat_nam',)
    #    #exclude = ('itemuser',)



class AdditemForm(forms.ModelForm):
    # model = Category

    class Meta:
        model = Items
        exclude = ('itemuser','years_used',)

