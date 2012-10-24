from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from application.models import *
from models import *
from forms import *

def first(request):
    output = {}
    form = FirstForm()

    if request.POST:
        form = FirstForm(request.POST)
        if form.is_valid():
            form.save()

    output['form'] = form
    
    return render_to_response('feedback/first.html', output, context_instance=RequestContext(request))
