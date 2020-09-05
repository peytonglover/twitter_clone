from django import forms
from twitteruser.models import TwitterUser

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
    tagname = forms.CharField(max_length=80)
    bio = forms.CharField(max_length=140)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)