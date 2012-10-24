from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django import forms
from models import *

class FirstForm(forms.Form):

    email = forms.EmailField(label=_("Email"), required=True)
    problem = forms.CharField(label=_("Describe the problem:"), required=True, widget=forms.Textarea())
    is_blocker =forms.BooleanField(label=_("Does this error disallows application to resume?"))

    def save(self, commit=True):

        email = self.cleaned_data["email"]
        problem = self.cleaned_data["problem"]
        is_blocker = self.cleaned_data["is_blocker"]

        user, created = User.objects.get_or_create(email=email, username=email)

        feedback = Feedback(creator=user, updater=user)
        feedback.problem = problem
        feedback.is_blocker = is_blocker
        feedback.save()

class SecondForm(forms.ModelForm):
    
    class Meta:
        model = AditionalFeedback
        exclude = ['updated', 'updater']

    feedback = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super(SecondForm, self).clean()
        cleaned_data["feedback"] = Feedback.objects.get(id=cleaned_data["feedback"])
        return cleaned_data
