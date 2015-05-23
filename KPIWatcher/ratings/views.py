from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *

def top_ratings(request):
	teachers = Teacher.objects.all().order_by('-avg_rating')
	return render(request, 'ratings/top_ratings.html', {'teachers': teachers})


def teacher_page(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'ratings/teacher_page.html', {'teacher': teacher, 'range': range(1, 11)})


def vote(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.vote(int(request.POST['vote']), request.user.student)
    return HttpResponseRedirect(reverse('teacher_page', kwargs={'pk': teacher.pk}))
