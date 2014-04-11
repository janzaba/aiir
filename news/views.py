# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from POVRay.news.models import *


def index(request):
    return render_to_response('index.html',
            {'zmienna': 'Jestem widokiem'},
            context_instance=RequestContext(request))