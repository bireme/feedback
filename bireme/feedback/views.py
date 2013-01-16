from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from application.models import *
from django.http import Http404
from models import *
from forms import *
from django.http import HttpResponse

def index(request):

    output = {}
    softwares = Application.objects.all()

    output['softwares'] = softwares

    return render_to_response('feedback/index.html', output, context_instance=RequestContext(request))        

def first(request, software):
    output = {}
    software = get_object_or_404(Application, slug=software)

    error = False
    if 'error' in request.GET and request.GET.get('error') == 1:
        error = True
    
    version = None
    if 'v' in request.GET:
        version = request.GET.get('v')
    
    referer = ""
    if 'HTTP_REFERER' in request.META:
        referer = request.META['HTTP_REFERER']

    site = ""
    if 'site' in request.GET:
        site = request.GET.get('site')

    form = FirstForm(initial={'software': software.id, 'version': version, 
        'ip': request.META['REMOTE_ADDR'], 'referer': referer, 'site': site, 'is_error': error})

    if request.POST:
        form = FirstForm(request.POST)
        if form.is_valid():
            form.save()

            try:
                user = User.objects.get(email=request.POST.get('email'))
                feedback = Feedback.objects.filter(creator=user)
                feedback = feedback[feedback.count()-1]
            except Exception as e:
                raise Http404

            return redirect(reverse("feedback.views.second", kwargs={'feedback': feedback.id}))

    output['form'] = form
    output['software'] = software

    return render_to_response('feedback/first.html', output, context_instance=RequestContext(request))    

def second(request, feedback):

    output = {}
    feedback = get_object_or_404(Feedback, id=feedback)
    another = Objective.objects.filter(is_another=True)[0]

    if AditionalFeedback.objects.filter(feedback=feedback):
        raise Http404

    initial_data = {
        "feedback": feedback.id,
        'name': feedback.creator.first_name,
        'age': feedback.creator.get_profile().age,
        'occupation': feedback.creator.get_profile().occupation,
    }

    form = SecondForm(initial=initial_data)

    if request.POST:
        form = SecondForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse("feedback_thanks"))

    output['another'] = another
    output['form'] = form
    output['feedback'] = feedback

    return render_to_response('feedback/second.html', output, context_instance=RequestContext(request))    
