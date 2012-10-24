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

    problem = models.TextField(_("problem"))
    blocker_error = models.BooleanField(_("is blocker error?"))
    software = models.ForeignKey(Version, verbose_name=_("Software"))

    def __unicode__(self):
        problem = self.problem[:20]
        if len(self.problem) > 20:
            problem += "..."
        return unicode(problem)

class AditionalFeedback(Generic):

    class Meta:
        verbose_name = _("aditional feedback")
        verbose_name_plural = _("aditionals feedback")

    feedback = models.ForeignKey(Feedback, unique=True)
    objective = models.ForeignKey(Objective, null=True, blank=True, verbose_name=_("What is the purpose of your search in VHL?"))
    regular_user = models.BooleanField(_("Regular User?"), default=False)
    how_should_work = models.TextField(_("how this site should work?"), null=True, blank=True)


