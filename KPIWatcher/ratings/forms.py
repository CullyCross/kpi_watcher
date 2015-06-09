from django import forms
from django.contrib.auth.models import User
from events.models import Company
from ratings.models import Teacher, Student

__author__ = 'cullycross'

from django.forms.models import model_to_dict, fields_for_model, ModelForm


class TeacherDetailsForm(ModelForm):
    pass


class StudentDetailsForm(ModelForm):
    pass


class CompanyDetailsForm(ModelForm):
    pass
