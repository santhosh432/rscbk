from django import forms

from .models import *


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['customer_name']


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    mobile = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','mobile', 'password1', 'password2',)


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    def clean_password(self):
        User = cache.get_model('auth', 'User')
        user = User.objects.get(username__exact=self.username)
        valid = user.check_password(self.cleaned_data['old_password'])
        if not valid:
            raise forms.ValidationError("Password Incorrect")
        return valid

    class Meta:
        model = User
        fields = ('old_password',)





class UserProfileForm(forms.ModelForm):
    user_image = forms.ImageField(widget=forms.FileInput)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserFullProfile
        fields = ('mobile','city', 'country','user_image') #Note that we didn't mention user field here.

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile




