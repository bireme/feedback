#! coding: utf-8
from django_tools.middlewares.ThreadLocal import get_current_user, get_current_request
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.db.models import signals
from django.template.defaultfilters import slugify

class Generic(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(_("created"), auto_now_add=True, editable=False)
    updated = models.DateTimeField(_("updated"), auto_now=True)
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
    slug = models.SlugField(max_length=255, blank=True)
    responsible = models.EmailField(_("responsible"))

    def __unicode__(self):
        return unicode(self.name)

def application_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)
signals.pre_save.connect(application_pre_save, sender=Application)