from django_tools.middlewares.ThreadLocal import get_current_request
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.db.models import signals
from django.conf import settings
from models import *

def send_email(sender, instance, created, **kwargs):

    prefix = "[BIREME FEEDBACK]"
    TITLE_RESPONSIBLE = _("%s New feedback" % prefix)
    TITLE_USER = _("%s Feedback was registered" % prefix)
    TITLE_FOLLOWUP = _("%s Your feedback was updated" % prefix)

    feedback = instance
    request = get_current_request()
    output = {
        'feedback': feedback,
    }

    if created:
        if feedback.application.responsible:
            email = feedback.application.responsible
            template = render_to_string("email/responsible.txt", output, context_instance=RequestContext(request)) 
            title = TITLE_RESPONSIBLE

            try:
                msg = EmailMessage(title, template, settings.EMAIL_FROM, [email])
                msg.content_subtype = "html"
                msg.send()
            except Exception as e:
                logger_logins = logging.getLogger('logview.userlogins')
                logger_logins.error(e)

        if feedback.creator.email:
            email = feedback.creator.email
            template = render_to_string("email/user.txt", output, context_instance=RequestContext(request)) 
            title = TITLE_USER    

            from_ = settings.EMAIL_FROM
            if feedback.application.responsible:
                from_ = feedback.application.responsible

            try:
                msg = EmailMessage(title, template, from_, [email])
                msg.content_subtype = "html"
                msg.send()
            except Exception as e:
                logger_logins = logging.getLogger('logview.userlogins')
                logger_logins.error(e)

    else:
        if feedback.creator.email:
            email = feedback.application.responsible
            template = render_to_string("email/followup.txt", output, context_instance=RequestContext(request)) 
            title = TITLE_FOLLOWUP

            from_ = settings.EMAIL_FROM
            if feedback.application.responsible:
                from_ = feedback.application.responsible

            try:
                msg = EmailMessage(title, template, from_, [email])
                msg.content_subtype = "html"
                msg.send()
            except Exception as e:
                logger_logins = logging.getLogger('logview.userlogins')
                logger_logins.error(e)

signals.post_save.connect(send_email, sender=Feedback, dispatch_uid="some.unique.string.id")