from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ratings.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^companies/(?P<pk>[0-9]+)', 'events.views.company_page'),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login", kwargs={'template_name': 'post_login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)
