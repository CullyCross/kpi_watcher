from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.top_ratings),
    url(r'^teacher/(?P<pk>[0-9]+)/$', views.teacher_page, name="teacher_page"),
    url(r'^teacher/(?P<pk>[0-9]+)/vote/$', views.vote, name="teacher_vote_url"),
]