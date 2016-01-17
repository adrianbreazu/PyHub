from django.conf.urls import patterns, url

urlpatterns = patterns(
    'django.contrib.auth.views',
    url(r'^login/$', 'login', name='login', kwargs={'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'logout', name='logout', kwargs={'next_page': '/'}),
)