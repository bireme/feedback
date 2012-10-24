#! coding: utf-8
from django_tools.middlewares.ThreadLocal import get_current_user, get_current_request
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Generic(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(_("created"), default=datetime.now(), editable=False)
    updated = models.DateTimeField(_("updated"), default=datetime.now())
    creator = models.ForeignKey(User, null=True, blank=True, related_name="+", default=get_current_user(), editable=False)
    updater = models.ForeignKey(User, null=True, blank=True, related_name="+", default=get_current_user())

    def save(self):
        self.updated = datetime.now()
        if not get_current_user().is_anonymous():
            self.updater = get_current_user()
        super(Generic, self).save()

class Application(Generic):

    class Meta:
        verbose_name = _("application")
        verbose_name_plural = _("applications")

    name = models.CharField(_("name"), max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class Version(Generic):
    
    class Meta:
        verbose_name = _("version")
        verbose_name_plural = _("versions")

    application = models.ForeignKey(Application, verbose_name=_("application"))
    version = models.CharField(_("version"), max_length=255)
    
    def __unicode__(self):
        return unicode(self.version)        
