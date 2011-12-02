import sys
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
from platform import uname


sys.path.insert(0, PROJECT_PATH + "../lib/python2.7")

# fabric 
from fabric.api import *
from fabric.main import display_command as _display_command

# from django.core.management import setup_environ

from pdb import set_trace as st

dev_django = "python manage.py %s --settings=settings"
prod_django = "python manage.py %s --settings=settings"

# local src directory
srcdir = "src"

## email address for user created.
admin_email = "admin@group6.net"

# for use with virtualenv
srccmd = "source %s/bin/activate" % PROJECT_PATH

# the database name
dbname = "elephanttalk"

### Utility functions ###
def _get_ip():
    """Pick out the ip address from a lineup, based upon platform type."""
    
    ## grep string for going through the interfaces until we find the active address
    ip_grep = 'grep "inet " | grep -v 127.0.0.1 | grep -v 172.16 | grep -v 192.168.169'
    
    ## depending on the platform, we take action.
    platform = uname()[0].lower()
    if platform == "linux":
        ## special casing for linux.
        output = local("ifconfig | %s" % ip_grep, capture=True)
        raw_address = output.strip().split(" ")[1]
        ip_address = raw_address.split(":")[-1]
    else:
        ## Assume OSX as default.
        ## command line for figuring out the ip address of the local dev machine.
        ip_command = 'ifconfig | %s | cut -d\  -f2 | head -1' % ip_grep
        ip_address = local(ip_command, capture=True)

    return ip_address.strip()

# def _set_admin_password(password):
# 
#     sys.path.append(srcdir)
#     import settings
#     setup_environ(settings)
# 
#     from django.contrib.auth.models import User
# 
#     u = User.objects.get(username__exact='admin')
#     u.set_password(password)
#     u.save()

def clean_db():
    """Deletes db, runs syncdb, adds user. NOTE: DATA LOSS
    """
    
    # string arguments for django to create the admin user
    create_admin_cmd = 'createsuperuser --noinput --username admin --email %s' % admin_email

    # drop and create the db from scratch.
    with prefix("export PGPASSWORD=conf/pgpassfile"):
        
        # check for an existing database.  If it exists, drop it.
        output = local("psql --list", capture=True)
        if dbname in output:
            local("dropdb %s" % dbname)
        
        # create our database
        local("createdb %s" % dbname)

    with lcd(srcdir):
        # run syncdb with no input
        local(dev_django % 'syncdb --noinput')
        
        # run migrations
        local(dev_django % 'migrate')
                
        # create the admin user with no password
        local(dev_django % create_admin_cmd)
    
    # run a script to create a password for the admin user.
#     _set_admin_passsword('password')
        
def refresh(mode=None):
    """Runs clean_db, load_data and testserver.
    
    You can pass it an additional arg (just like with the testserver command)
    for mobile or api test server work.
    
    Example:
        
        fab refresh:api
        fab refresh:mobile
    """
    clean_db()
    #load_data()
#     testserver(mode)

def testserver():
    """Run the test server.
    """

    args = 'runserver %s:8000' % _get_ip()
    django = dev_django
    try:
        with lcd(srcdir):
             local(django % args, capture=False)
    except:
        raise

