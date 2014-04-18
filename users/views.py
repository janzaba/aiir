# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Adres email",widget=forms.TextInput(attrs={'class': 'form-control input-md'}))
    name = forms.CharField(max_length=150,label="Imię i nazwisko / Nick / Nazwa konta",widget=forms.TextInput(attrs={'class': 'form-control input-md'}))
    password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class': 'form-control input-md'}),label="Hasło",)
    re_password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class': 'form-control input-md'}),label="Powtórz hasło")

class LoginForm(forms.Form):
    email = forms.EmailField(label="Adres email",widget=forms.TextInput(attrs={'class': 'form-control input-md'}))
    password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class': 'form-control input-md'}),label="Hasło",)

def register(request):
    f = RegisterForm()
    return render_to_response('register.html',
            {'form': f, 'menu':'register'},
            context_instance=RequestContext(request))

def login(request):
    f = LoginForm()
    return render_to_response('login.html',
            {'form': f, 'menu':'login'},
            context_instance=RequestContext(request))