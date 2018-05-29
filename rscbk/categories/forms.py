#from django.forms import ModelForm
from django import forms
from .models import *
from home.models import *

class AddwishlistForm(forms.ModelForm):
    #model = Brand

    class Meta:
        model = Wishlist
        fields = ('wishlist_category','wishlist_name','wishlist_full_desc','wishlist_other_info')
        exclude = ('wishlist_user',)

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

    def __init__(self, *args, **kwargs):
        self.category = Category.objects.exclude(category_name='Cash')
        super(AdditemForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = self.category

