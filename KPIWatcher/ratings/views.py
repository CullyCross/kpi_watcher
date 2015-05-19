from django.shortcuts import render, get_object_or_404
from .models import *

def top_ratings(request):
	teachers = Teacher.objects.all().order_by('avg_rating')
	return render(request, 'ratings/top_ratings.html', {'teachers': teachers})


def teacher_page(request, pk):
	teacher = get_object_or_404(Teacher, pk=pk)
	return render(request, 'ratings/teacher_page.html', {'teacher': teacher})


def vote_for_teacher(request, pk):
	pass