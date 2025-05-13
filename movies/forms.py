from django import forms

class RegistrationForm(forms.Form):
    nickname = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

class LoginForm(forms.Form):
    nickname = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)