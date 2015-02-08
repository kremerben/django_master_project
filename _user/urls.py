from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_name.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^profile/$', '_user.views.profile_by_username', name='profile'),
    url(r'^profile/(?P<profile_username>[-\w\ !.]+)/$', '_user.views.profile_by_username', name='profile_by_username'),
    url(r'^profile/(?P<profile_username>[-\w\ !.]+)/update/$', '_user.views.profile_update', name='profile_update'),

    # LOGIN AND LOGOUT
    url(r'^register/$', '_user.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),


    # USER AUTHENTICATION #
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),



)
