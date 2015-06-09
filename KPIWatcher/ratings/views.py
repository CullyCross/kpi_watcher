from django.contrib.auth import login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from ratings.forms import TeacherDetailsForm, CompanyDetailsForm, StudentDetailsForm


def top_ratings(request):
	teachers = Teacher.objects.all().order_by('-avg_rating')[:100]
	return render(request, 'ratings/top_ratings.html', {'teachers': teachers})


def teacher_page(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if hasattr(request.user, 'student'):
        perm_to_vote = True
    else:
        perm_to_vote = False

    return render(request, 'ratings/teacher_page.html', {'teacher': teacher, 'range': range(1, 11), 'perm_to_vote': perm_to_vote})


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
            message = "You can't vote!"
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


def basic_register(request):
    return render(request, 'ratings/basic_registration.html')


def registration(request):

    if request.method == "POST":
        reg_type = request.POST.get('post_reg_type', '')

        if reg_type == 'teacher':
            form = TeacherDetailsForm(request.POST)
            if form.is_valid():
                teacher = form.save(commit=False)
                teacher.save()
                login(request, teacher.user)
                return redirect('ratings.views.teacher_page', pk=teacher.pk)
        elif reg_type == 'company':
            form = CompanyDetailsForm(request.POST)
            if form.is_valid():
                company = form.save(commit=False)
                company.save()
                login(request, company.user)
                return redirect('events.views.company_page', pk=company.pk)
        else:
            form = StudentDetailsForm(request.POST)
            if form.is_valid():
                student = form.save(commit=False)
                student.save()
                login(request, student.user)
                return redirect('ratings.views.student_page', pk=student.pk)
        return render(request, 'ratings/registration.html', {'form_reg': form, 'reg_type': reg_type})

    elif request.method == "GET":
        reg_type = request.GET.get('type', '')

        if not request.user.is_authenticated():
            if reg_type == 'teacher':
                form = TeacherDetailsForm()
            elif reg_type == 'company':
                form = CompanyDetailsForm()
            else:
                form = StudentDetailsForm()
            return render(request, 'ratings/registration.html', {'form_reg': form, 'reg_type': reg_type})






