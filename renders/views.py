# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

import json

from POVRay.renders.models import Renders

def render(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/register')
    else:
        return render_to_response('create.html',{},context_instance=RequestContext(request))

def my_renders(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/register')
    else:
        return render_to_response('my_renders.html',{},context_instance=RequestContext(request))
def ajax(request, action):
    response = {}
    response['result'] = 'failed'
    if not request.user.is_authenticated():
        response['message'] = 'brak zalogowanego użytkownika'
        return render_to_response('ajax.html',{'response':json.dumps(response)},context_instance=RequestContext(request))
    else:
        if action == "create":
            #dodanie renderu do bazy danych
            if request.method == 'POST':
                r = Renders(user=request.user,script=request.POST['script'])
                r.save()
                if r.id:
                    response['result'] = 'success'
                else:
                    response['message'] = 'błąd dodania renderu do bazy danych'
            else:
                response['message'] = 'brak danych'
        else:
            response['message'] = 'nie rozpoznano akcji'
        return render_to_response('ajax.html',{'response':json.dumps(response)},context_instance=RequestContext(request))