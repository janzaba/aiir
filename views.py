# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Adres email")
    name = forms.CharField(max_length=150,label="Imię i nazwisko / Nick / Nazwa konta")
    password = forms.CharField(max_length=150,widget=forms.PasswordInput(),label="Hasło")
    re_password = forms.CharField(max_length=150,widget=forms.PasswordInput(),label="Powtórz hasło")

def index(request):
    return render_to_response('index.html',
            {},
            context_instance=RequestContext(request))

def register(request):
    f = RegisterForm()
    return render_to_response('register.html',
            {'f': f.as_p()},
            context_instance=RequestContext(request))