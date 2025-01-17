from django import forms
from django.forms import ModelForm
from instauser.models import InstaUser


class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = InstaUser
        fields = ["username","display_name","password"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)