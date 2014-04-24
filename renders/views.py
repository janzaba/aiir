# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def render(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/register')
    else:
        if request.method == 'POST':
            #przesłano formularz - dodaję skrypt do bazy
            return render_to_response('create.html',{},context_instance=RequestContext(request))
        else:
            #nie przesłano formularza
            return render_to_response('create.html',{},context_instance=RequestContext(request))