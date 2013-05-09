from django_tools.middlewares.ThreadLocal import get_current_request
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from application.models import *
from util.models import *
from django.db import models
import md5

class Category(Generic):
    """ Categories who selected by admin """

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    name = models.CharField(_("category"), max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class Feedback(Generic):

    class Meta:
        verbose_name = _("feedback")
        verbose_name_plural = _("feedbacks")


    problem = models.TextField(_("problem"))
    blocker_error = models.BooleanField(_("is blocker error?"))
    application = models.ForeignKey(Application, verbose_name=_("Software"))
    version = models.CharField(max_length=255, verbose_name=_("Version"), null=True, blank=True)
    ip = models.CharField(_("ip"), max_length=255)
    referer = models.CharField(_("referer"), max_length=255, null=True, blank=True)
    site = models.CharField(_('id site'), max_length=255, null=True, blank=True)
    is_error = models.BooleanField(_("is a error?"))
    staff_comment = models.TextField(_("staff comment"), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    answer = models.TextField(_("answer"), blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)

    def __unicode__(self):
        problem = self.problem[:20]
        if len(self.problem) > 20:
            problem += "..."
        return unicode(problem)
    
    def get_absolute_url(self):
        
        request = get_current_request()
        url = reverse('feedback.views.show', kwargs={'feedback': self.id})
        url = "http://%s%s" % (request.META['HTTP_HOST'], url)

        if ":3001" in url:
            url = url.replace(":3001", "")

        return url

class AditionalFeedback(Generic):

    REGULAR_CHOICES = (
        ('1', _('Once a week')),
        ('2', _('Twice a month')),
        ('3', _('Once a month')),
        ('4', _('Once in a while')),
        ('5', _('Rarely')),
    )

    OBJECTIVE_CHOICES = (
        ('1', _("Professional training/Study")),
        ('2', _("Academic /Teaching")),
        ('3', _("Scientific research")),
        ('4', _("Healthcare")),
        ('5', _("Decision making")),
        ('6', _("Project management")),
        ('7', _("Knowledge /Information management")),
        ('8', _("Bibliographic search")),
    )

    class Meta:
        verbose_name = _("aditional feedback")
        verbose_name_plural = _("aditionals feedback")

    objective = models.CharField(null=True, blank=True, verbose_name=_("What your primary interest for using a VHL service or product?"), choices=OBJECTIVE_CHOICES, max_length=255)
    regular_user = models.CharField(_("Regular User?"), blank=True, null=True, choices=REGULAR_CHOICES, max_length=255)
    how_should_work = models.TextField(_("how this site should work?"), null=True, blank=True)
    another_objective = models.CharField(_("Describe your purpose to use our applications"), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)


