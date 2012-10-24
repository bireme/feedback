from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from application.models import *
from django.http import Http404
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

def second(request, feedback):

    output = {}
    feedback = get_object_or_404(Feedback, id=feedback)

    if AditionalFeedback.objects.filter(feedback=feedback):
        raise Http404

    aditional = AditionalFeedback(feedback=feedback)
    form = SecondForm(instance=aditional)

    if request.POST:
        form = SecondForm(request.POST)
        if form.is_valid():
            form.save()

    output['form'] = form
    output['feedback'] = feedback

    return render_to_response('feedback/second.html', output, context_instance=RequestContext(request))    
