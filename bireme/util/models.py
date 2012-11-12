from django.db import models
from application.models import Generic
from django.utils.translation import ugettext_lazy as _

class Country(Generic):

	class Meta:
		verbose_name = _("country")
		verbose_name_plural = _("countries")

	name = models.CharField(_("name"), max_length=255)
	code = models.CharField(_("code"), max_length=255)

	def __unicode__(self):
		return "%s - %s" % (unicode(self.code), unicode(self.name))