# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
# from bson import json_util

import json
import os

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

@csrf_exempt
def ajax(request, action):

    response = {}
    response['result'] = 'failed'
    if not request.user.is_authenticated():
        response['message'] = 'brak zalogowanego użytkownika'
    else:
        if action == "create":
            #dodanie renderu do bazy danych
            if request.method == 'POST':
                r = Renders(user=request.user,script=request.POST['script'],name=request.POST['name'])
                r.status = "created"
                r.save()
                #CREATING FOLDER FOR THE RENDER
                path = os.path.join('/home/aiir/POVRay/static/users/', str(request.user.id))
                path = os.path.join(path, str(r.id))
                os.mkdir(path)
                #CREATING RENDER FILES
                f = open(os.path.join(path, 'scena.pov'), 'w')
                file = File(f)
                file.write(r.script)
                file.closed
                f.closed
                if r.id:
                    response['result'] = 'success'
                else:
                    response['message'] = 'błąd dodania renderu do bazy danych'
            else:
                response['message'] = 'brak danych'
        elif action == "select":
            r = Renders.objects.filter(user = request.user)
            response = []
            for render in r:
                tmp = {}
                tmp['id'] = render.id
                tmp['name'] = render.name
                tmp['start_date'] = str( render.start_date )
                #tmp['end_date'] = str( render.end_date )
                tmp['end_date'] = str( render.status )
                response.append(tmp)
        elif action == "refresh":
            r = Renders.objects.filter(user = request.user)
            for render in r:
                path = os.path.join('/home/aiir/POVRay/static/users/', str(request.user.id))
                path = os.path.join(path, str(render.id))
                path = os.path.join(path, "scena.png")
                if os.path.isfile(path):
                    #render complited
                    render.status = "done"
                    render.save()
                    response['result'] = 'success'
        else:
            response['message'] = 'nie rozpoznano akcji'
    return HttpResponse(json.dumps(response), mimetype="application/json")