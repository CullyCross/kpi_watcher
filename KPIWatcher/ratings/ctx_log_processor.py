__author__ = 'cullycross'

from django.contrib.admin.forms import AuthenticationForm as AuthForm

def auth_form(request):
    return {'form': AuthForm(), 'request': request}
