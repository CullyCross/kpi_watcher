from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.top_ratings, name="all_teachers"),
    url(r'^teacher/(?P<pk>[0-9]+)/$', views.teacher_page, name="teacher_page"),
    url(r'^teacher/(?P<pk>[0-9]+)/vote/$', views.vote, name="teacher_vote_url"),
    url(r'^students/$', views.students_all, name="all_students"),
    url(r'^students/(?P<pk>[0-9]+)/$', views.student_page, name="student_page"),
    url(r'^choose_your_hero/', views.basic_register, name="basic_register"),
    url(r'^registration/', views.registration, name="registration"),
    url(r'^university/', views.university, name="university"),
    url(r'^groups/(?P<pk>[0-9]+)/$', views.group_page, name="group_page"),
    url(r'^groups/(?P<pk>[0-9]+)/vote/$', views.vote_group, name="group_vote_url"),
    url(r'^groups/', views.all_groups, name="all_groups"),
]