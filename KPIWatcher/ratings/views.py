from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from events.forms import CompanyDetailsForm
from events.models import Company
from .models import *
from ratings.forms import TeacherDetailsForm, StudentDetailsForm, UserDetailsForm


#todo: group page (and vote also)
#todo: links in university page, etc

def top_ratings(request):
	teachers = Teacher.objects.all().order_by('-avg_rating')[:100]
	return render(request, 'ratings/top_ratings.html', {'teachers': teachers})


def teacher_page(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if hasattr(request.user, 'student'):
        perm_to_vote = True
        perm_to_comment = True
    else:
        perm_to_vote = False
        perm_to_comment = False

    return render(request, 'ratings/teacher_page.html',
                  {'teacher': teacher, 'range': range(1, 11),
                   'perm_to_vote': perm_to_vote, 'perm_to_comment': perm_to_comment})


def vote(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.POST and not request.user.is_anonymous():
        if hasattr(request.user, 'student'):
            voted = teacher.vote(int(request.POST['vote']), request.user.student)
            perm_to_comment = True
            if voted:
                message = "Success"
            else:
                message = "You've already voted"
        else:
            perm_to_comment = False
            message = "You can't vote!"
    else:
        message = "Error!"
    return render(request, 'ratings/teacher_page.html',
                  {'teacher': teacher, 'range': range(1, 11),
                   'message': message, 'perm_to_comment': perm_to_comment})


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

        user_form = UserDetailsForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            if reg_type == 'teacher':
                form = TeacherDetailsForm(request.POST)
                if form.is_valid():
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    user.save()
                    department = form.cleaned_data['department']
                    teacher = Teacher.objects.create(user=user, department=department)
                    teacher.user = user
                    teacher.save()
                    login(request, user)
                    return redirect('ratings.views.teacher_page', pk=teacher.pk)
            elif reg_type == 'company':
                form = CompanyDetailsForm(request.POST)
                if form.is_valid():
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    user.save()
                    name = form.cleaned_data['name']
                    description = form.cleaned_data['description']
                    company = Company.objects.create(user=user, name=name, description=description)
                    company.user = user
                    company.save()
                    login(request, user)
                    return redirect('events.views.company_page', pk=company.pk)
            else:
                form = StudentDetailsForm(request.POST)
                if form.is_valid():
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    user.save()
                    group = form.cleaned_data['group']
                    is_leader = form.cleaned_data['is_leader']
                    student = Student.objects.create(user=user, group=group, is_leader=is_leader)
                    student.save()
                    login(request, user)
                    return redirect('ratings.views.student_page', pk=student.pk)
            return render(request, 'ratings/registration.html',
                          {'form_reg': form, 'form_user': user_form, 'reg_type': reg_type})

    elif request.method == "GET":
        reg_type = request.GET.get('type', '')

        if not request.user.is_authenticated():
            user_form = UserDetailsForm()
            if reg_type == 'teacher':
                form = TeacherDetailsForm()
            elif reg_type == 'company':
                form = CompanyDetailsForm()
            else:
                form = StudentDetailsForm()
            return render(request, 'ratings/registration.html',
                          {'form_type': form, 'form_user': user_form, 'reg_type': reg_type})
    return redirect('/')


def university(request):
    kpi = University.objects.all().first()
    kpi.count_rating()
    return render(request, 'ratings/university.html', {'university': kpi})


def all_groups(request):
    groups_all = Group.objects.all()
    paginator = Paginator(groups_all, 25)

    page = request.GET.get('page')

    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        groups = paginator.page(paginator.num_pages)

    return render(request, 'ratings/all_groups.html', {'groups': groups})


def group_page(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if hasattr(request.user, 'teacher'):
        perm_to_vote = True
        perm_to_comment = True
    else:
        perm_to_vote = False
        perm_to_comment = False

    return render(request, 'ratings/group_page.html',
                  {'group': group, 'range': range(1, 11),
                   'perm_to_vote': perm_to_vote, 'perm_to_comment': perm_to_comment})

def vote_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.POST and not request.user.is_anonymous():
        if hasattr(request.user, 'teacher'):
            perm_to_comment = True
            voted = group.vote(int(request.POST['vote']), request.user.teacher)
            if voted:
                message = "Success"
            else:
                message = "You've already voted"
        else:
            perm_to_comment = False
            message = "You can't vote!"
    else:
        message = "Error!"
    return render(request, 'ratings/group_page.html',
                  {'group': group, 'range': range(1, 11),
                   'message': message, 'perm_to_comment': perm_to_comment})