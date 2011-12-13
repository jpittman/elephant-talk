
To set up the development environment, do the following:

1. With fabfile, run: 
    fab refresh.
2. Change the admin's password with django management script:
    ./manage.py changepassword admin
3. With fabfile, run:
    fab testserver
    
todo
====

 - add a profile pic for users
 - associate a user with a comment if the user is logged in.
 - add support for markdown syntax into blog posts
 
known issues
====

 - jquery mobile is doing some caching of views.  It causes some pages have content previously
 viewed or edited (in the case of a form).