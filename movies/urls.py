from django.shortcuts import render

from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome),
    path('main_page/',views.main_page,name='main_page'),

    path('registration/',views.registration_page, name='registration'),
    path('register/',views.registration_view,name='register'),

    path('login/',views.login_page,name='login'),
    path('login_request/',views.login_view,name='login_request'),
]
