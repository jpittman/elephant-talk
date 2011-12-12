
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