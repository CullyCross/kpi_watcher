from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *

def top_ratings(request):
	teachers = Teacher.objects.all().order_by('-avg_rating')[:100]
	return render(request, 'ratings/top_ratings.html', {'teachers': teachers})


def teacher_page(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'ratings/teacher_page.html', {'teacher': teacher, 'range': range(1, 11)})


def vote(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.POST and not request.user.is_anonymous():
        if hasattr(request.user, 'student'):
            voted = teacher.vote(int(request.POST['vote']), request.user.student)
            if voted:
                message = "Success"
            else:
                message = "You've already voted"
        else:
            message = "Teacher can't vote!"
    else:
        message = "Error!"
    return render(request, 'ratings/teacher_page.html', {'teacher': teacher, 'range': range(1, 11), 'message': message})


def student_page(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'ratings/student_page.html', {'student': student})

def students_all(request):
    students_all_list = Student.objects.all().order_by('user__username')
    paginator = Paginator(students_all_list, 25)

    page = request.GET.get('page')

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'ratings/all_students.html', {'students': students})
