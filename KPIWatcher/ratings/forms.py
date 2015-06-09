from django import forms
from django.contrib.auth.models import User
from events.models import Company
from ratings.models import Teacher, Student

__author__ = 'cullycross'

from django.forms.models import model_to_dict, fields_for_model, ModelForm


class TeacherDetailsForm(ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Re-enter password", widget=forms.PasswordInput)

    def __init__(self, instance=None, *args, **kwargs):
        _fields = ('first_name', 'last_name', 'email',)
        _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
        super(TeacherDetailsForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(fields_for_model(User, _fields))

    class Meta:
        model = Teacher
        fields = ('department', 'password', 'password2')

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(TeacherDetailsForm, self).save(*args,**kwargs)
        return profile

    def clean(self):
        form_data = self.cleaned_data

        try:
            User.objects.get(email_address = form_data['email'])
            raise forms.ValidationError("Email taken.")
        except User.DoesNotExist:
            pass

        if form_data['password'] != form_data['password2']:
            self._errors["password"] = ["Password do not match"] # Will raise a error message
            del form_data['password']
            del form_data['password2']
        return form_data


class StudentDetailsForm(ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Re-enter password", widget=forms.PasswordInput)

    def __init__(self, instance=None, *args, **kwargs):
        _fields = ('first_name', 'last_name', 'email',)
        _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
        super(StudentDetailsForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(fields_for_model(User, _fields))

    class Meta:
        model = Student
        fields = ('group', 'is_leader',  'password', 'password2')

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(StudentDetailsForm, self).save(*args,**kwargs)
        return profile

    def clean(self):
        form_data = self.cleaned_data

        try:
            User.objects.get(email_address = form_data['email'])
            raise forms.ValidationError("Email taken.")
        except User.DoesNotExist:
            pass

        if form_data['password'] != form_data['password2']:
            self._errors["password"] = ["Password do not match"] # Will raise a error message
            del form_data['password']
            del form_data['password2']
        return form_data


class CompanyDetailsForm(ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Re-enter password", widget=forms.PasswordInput)

    def __init__(self, instance=None, *args, **kwargs):
        _fields = ('first_name', 'last_name', 'email',)
        _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
        super(CompanyDetailsForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(fields_for_model(User, _fields))

    class Meta:
        model = Company
        fields = ('name', 'description', 'password', 'password2')

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.email = self.cleaned_data['email']
        u.set_password(self.cleaned_data['password'])
        u.save()
        profile = super(CompanyDetailsForm, self).save(*args, **kwargs)
        return profile

    def clean(self):
        form_data = self.cleaned_data

        try:
            User.objects.get(email_address = form_data['email'])
            raise forms.ValidationError("Email taken.")
        except User.DoesNotExist:
            pass

        if form_data['password'] != form_data['password2']:
            self._errors["password"] = ["Password do not match"] # Will raise a error message
            del form_data['password']
            del form_data['password2']
        return form_data
