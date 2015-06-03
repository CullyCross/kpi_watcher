from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.all_events),
    url(r'^(?P<pk>[0-9]+)/$', views.event_page, name="event_page"),
    #url(r'^(?P<pk>[0-9]+)/subscribe/$', views.subscribe, name="event_subscribe"),
]