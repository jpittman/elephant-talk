from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    
    # returns the profile for a specified user.
    (r'^edit_profile/', 'userprofile.views.edit_user_profile'),

    # returns the profile for a specified user.
    (r'^(?P<username>[\w]+)/$', 'userprofile.views.get_user_profile'),

    # default
    (r'', 'userprofile.views.list_users'),
)
