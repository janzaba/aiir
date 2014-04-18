# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django import forms


################################  FORMULARZE ###################################################################################################################################
class RegisterForm(forms.Form):
    email = forms.EmailField(label="Adres email",widget=forms.TextInput(attrs={'class': 'form-control input-md'}))
    name = forms.CharField(max_length=150,label="Imię i nazwisko / Nick / Nazwa konta",widget=forms.TextInput(attrs={'class': 'form-control input-md'}))
    password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class': 'form-control input-md'}),label="Hasło",)
    re_password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class': 'form-control input-md'}),label="Powtórz hasło")

class LoginForm(forms.Form):
    email = forms.EmailField(label="Adres email",widget=forms.TextInput(attrs={'class': 'form-control input-md'}))
    password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class': 'form-control input-md'}),label="Hasło",)

################################  HOME ###################################################################################################################################
def index(request):
        return render_to_response('index.html',{'menu':'home','user':request.user},context_instance=RequestContext(request))

################################  REGISTER ###################################################################################################################################
def register(request):
    formErrors = []
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['re_password']:                   #czy wpisane hasła są takie same
                same_emails = User.objects.get(username__exact=form.cleaned_data['email'])        #sprawdzam czy występuje już użytkownik o tym mailu
                if not same_emails:                                                                #jeśli nie
                    user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['password'])
                    user.first_name = form.cleaned_data['name']
                    user.is_staff = False
                    user.save()
                    return HttpResponseRedirect('/login')
                else:
                    formErrors.append("Podany adres email istnieje już w naszej bazie danych");
                    return render_to_response('register.html',{'form': form, 'menu':'login', 'formErrors':formErrors, 'user':request.user},context_instance=RequestContext(request))
            else:
                formErrors.append("Wpisane hasła różnią się od siebie");
                return render_to_response('register.html',{'form': form, 'menu':'login', 'formErrors':formErrors, 'user':request.user},context_instance=RequestContext(request))

        else:
            return render_to_response('register.html',{'form': form, 'menu':'login'},context_instance=RequestContext(request))
    else:
        f = RegisterForm()
        return render_to_response('register.html',
                {'form': f, 'menu':'register','user':request.user},
                context_instance=RequestContext(request))

################################  LOGIN ###################################################################################################################################
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            f = LoginForm()
            return render_to_response('login.html',{'form': f, 'menu':'login', 'formErrors':'Błąd podczas logowania','user':request.user},context_instance=RequestContext(request))
    else:
        f = LoginForm()
        return render_to_response('login.html',
            {'form': f, 'menu':'login','user':request.user},
            context_instance=RequestContext(request))

################################  LOGOUT ###################################################################################################################################
def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/')