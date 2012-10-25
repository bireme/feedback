from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):

    AGE_CHOICES = (
        ('30', "less than 30"),
        ('between 30 and 45', "between 30 and 45"),
        ("more than 45", "more than 45"),
    )

    user = models.ForeignKey(User, unique=True)
    occupation = models.CharField(_("occupation"), max_length=255, blank=True, null=True)
    age = models.CharField(_("age"), max_length=255, blank=True, null=True, choices=AGE_CHOICES)

def create_profile(sender, instance, created, **kwargs):
    user = instance
    try:
        profile = user.get_profile()
    except:
        profile = UserProfile(user=user)
        profile.save()
models.signals.post_save.connect(create_profile, sender=User, dispatch_uid="some.unique.string.id")