from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.all_events),
    url(r'^(?P<pk>[0-9]+)/$', views.event_page, name="event_page"),
    url(r'^(?P<pk>[0-9]+)/subscribe/$', views.subscribe, name="event_subscribe"),
    url(r'^(?P<pk>[0-9]+)/unsubscribe/$', views.unsubscribe, name="event_unsubscribe"),
    url(r'^create/$', views.create_new, name="event_create"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.event_edit, name='event_edit'),
]