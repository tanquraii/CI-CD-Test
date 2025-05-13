from django.shortcuts import render, redirect
import requests
from .forms import RegistrationForm, LoginForm
from .models import CatUser
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def welcome(request):
    return render(request,'welcome_page.html')

def cat_display():
    response = requests.get("https://api.thecatapi.com/v1/images/search?limit=20&api_key=live_xiScVEjeRADlkOHb2mq2BRq0BSx7xuzj48qeLIUAYPjt3i6Za2dFXFVyn5EtLlEw")
    data = response.json()
    url = data[0]['url']
    return url

def registration_page(request):
    form = RegistrationForm()
    return render(request,'registration.html',{'form':form})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = CatUser()
            new_user.nickname = form.cleaned_data['nickname']
            new_user.password = form.cleaned_data['password']
            new_user.save()
            return redirect('main_page')
        else:
            return HttpResponse('form is invalid')
    return redirect('main_page')

def login_page(request):
    login_form = LoginForm()
    return render(request,'login.html',{'login_form':login_form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            password = form.cleaned_data['password']
            
            user = CatUser.objects.filter(nickname=nickname, password=password).first()
            
            if user:
                return redirect('main_page')
            else:
                return HttpResponse('Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def main_page(request):
    url = cat_display()
    return render(request,'index.html',{'url':url})
# Create your views here.
