from django.shortcuts import render
from .models import *

def top_ratings(request):
	teachers = Teacher.objects.all().order_by('avg_rating')
	return render(request, 'ratings/top_ratings.html', {'teachers': teachers})