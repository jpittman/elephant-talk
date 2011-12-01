from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elephant_talk.views.home', name='home'),
    # url(r'^elephant_talk/', include('elephant_talk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    ## auth
    (r'^login/$', 'django.contrib.auth.views.login'),    
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^change_password/$', 'django.contrib.auth.views.password_change', 
        {'template_name': 'registration/change_password.html', 
        'post_change_redirect':'/password_done/'}),
    (r'^password_done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'registration/password_success.html'}),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    # handling web crawlers.
    (r'^robots\.txt$', 
        lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
)
