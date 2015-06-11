from django.contrib.auth.models import User
from ratings.models import Teacher, Student

__author__ = 'cullycross'

from django.forms.models import ModelForm

class UserDetailsForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', )

class TeacherDetailsForm(ModelForm):

    class Meta:
        model = Teacher
        exclude = ('user', )


class StudentDetailsForm(ModelForm):

    class Meta:
        model = Student
        exclude = ('user', )


