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
    if request.GET.get('q'):
        return redirect(reverse('feedback.views.show', kwargs={'feedback': request.GET.get('q')}))

    if request.GET.get('application'):
        application = get_object_or_404(Application, slug=request.GET.get('application'))

    return render_to_response('feedback/index.html', output, context_instance=RequestContext(request))        

def first(request, software):
    output = {}
    software = get_object_or_404(Application, slug=software)

    error = False
    if 'error' in request.GET and request.GET.get('error') == '1':
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

            return redirect(reverse("feedback.views.thanks", kwargs={'feedback': feedback.id}))

    output['form'] = form
    output['software'] = software

    return render_to_response('feedback/first.html', output, context_instance=RequestContext(request))    

def second(request, feedback):

    output = {}
    feedback = get_object_or_404(Feedback, id=feedback)

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

            return redirect(reverse("feedback_thanks2", kwargs={'feedback': feedback.id}))

    output['form'] = form
    output['feedback'] = feedback

    return render_to_response('feedback/second.html', output, context_instance=RequestContext(request))

def thanks(request, feedback):

    output = {}
    feedback = get_object_or_404(Feedback, id=feedback)

    output['feedback'] = feedback
    return render_to_response('feedback/thanks.html', output, context_instance=RequestContext(request))

def thanks2(request, feedback):

    output = {}
    feedback = get_object_or_404(Feedback, id=feedback)

    output['feedback'] = feedback
    return render_to_response('feedback/thanks2.html', output, context_instance=RequestContext(request))

def show(request, feedback):

    output = {}
    feedback = get_object_or_404(Feedback, id=feedback) 

    if not feedback.is_active:
        raise Http404

    output['feedback'] = feedback
    return render_to_response('feedback/show.html', output, context_instance=RequestContext(request))


