#! coding:utf-8
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django import forms
from models import *
from application.models import *
from account.models import *

class FirstForm(forms.Form):

    email = forms.EmailField(label=_("Email"), required=True)
    problem = forms.CharField(label=_("Describe the problem:"), required=True, widget=forms.Textarea())
    is_blocker =forms.BooleanField(label=_("Does this error disallows application to resume?"), required=False)
    software = forms.CharField(widget=forms.HiddenInput(), required=False)

    def save(self, commit=True):

        email = self.cleaned_data["email"]
        problem = self.cleaned_data["problem"]
        is_blocker = self.cleaned_data["is_blocker"]
        software = self.cleaned_data["software"]

        user, created = User.objects.get_or_create(email=email, username=email)

        feedback = Feedback(creator=user, updater=user)
        feedback.problem = problem
        feedback.is_blocker = is_blocker
        feedback.software = Version.objects.get(id=software)
        feedback.save()

class SecondForm(forms.Form):
    
    feedback = forms.CharField(widget=forms.HiddenInput(), required=True)
    objective = forms.ModelChoiceField(queryset=Objective.objects.all(), label=_("What your purpose to use our applications?"), required=False)
    regular_user = forms.BooleanField(label=_("Are you a regular user?"), required=False)
    how_should_work = forms.CharField(label=_("how this site should work?"), widget=forms.Textarea(), required=False)

    name = forms.CharField(label=_("What's your name?"), required=False)
    occupation = forms.CharField(label=_("What is your occupation?"), required=False)
    age = forms.CharField(label=_("What's your age?"), widget=forms.Select(choices=UserProfile.AGE_CHOICES))

    def clean_feedback(self):
        cleaned_data = super(SecondForm, self).clean()
        cleaned_data["feedback"] = Feedback.objects.get(id=cleaned_data["feedback"])
        return cleaned_data

    def save(self, commit=True):

        data = self.cleaned_data

        if Feedback.objects.filter(id=self.data['feedback']):
            print "já existe"

        feedback = Feedback.objects.get(id=self.data['feedback'])
        
        add = AditionalFeedback(feedback=feedback)
        add.objective = data['objective']
        add.regular_user = data['regular_user']
        add.how_should_work = data['how_should_work']
        add.save()

        profile = UserProfile.objects.get(user=feedback.creator)
        profile.age = data['age']
        profile.occupation = data['occupation']
        profile.save()

        user = feedback.creator
        user.first_name = data['name']
        user.save()



