from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from application.models import *
from django.db import models

class Objective(Generic):

    class Meta:
        verbose_name = _("objective")
        verbose_name_plural = _("objectives")

    title = models.CharField(_("objective"), max_length=255)

    def __unicode__(self):
        return unicode(self.title)    

class SimilarSite(Generic):
    """ Sites similares """

    class Meta:
        verbose_name = _("similar site")
        verbose_name_plural = _("similar sites")

    feedback = models.ForeignKey("Feedback")
    url = models.URLField(_("address"))

    def __unicode__(self):
        return unicode(self.url)


class Feedback(Generic):

    class Meta:
        verbose_name = _("feedback")
        verbose_name_plural = _("feedbacks")

    user = models.ForeignKey(User, verbose_name=_("user"))
    problem = models.TextField(_("problem"))
    blocker_error = models.BooleanField(_("is blocker error?"))

    def __unicode__(self):
        return unicode(self.problem[:20])

class AditionalFeedback(Generic):

    class Meta:
        verbose_name = _("aditional feedback")
        verbose_name_plural = _("aditionals feedback")

    feedback = models.ForeignKey(Feedback, unique=True)
    objective = models.ForeignKey(Objective, null=True, blank=True)
    regular_user = models.BooleanField(_("Regular User?"), default=False)
    how_should_work = models.TextField(_("how this site should work?"), null=True, blank=True)


