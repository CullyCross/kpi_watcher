from django.shortcuts import render

def top_ratings(request):
	return render(request, 'ratings/top_ratings.html', {})