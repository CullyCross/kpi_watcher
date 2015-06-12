from django.contrib.auth.forms import UserCreationForm
from ratings.models import Teacher, Student

__author__ = 'cullycross'

from django.forms.models import ModelForm

class UserDetailsForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email', )

class TeacherDetailsForm(ModelForm):

    class Meta:
        model = Teacher
        exclude = ('user', )


class StudentDetailsForm(ModelForm):

    class Meta:
        model = Student
        exclude = ('user', )


