__author__ = 'cullycross'

from django.forms.models import ModelForm

from .models import Event, Company


class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'text', )

class CompanyDetailsForm(ModelForm):

    class Meta:
        model = Company
        exclude = ('user', )