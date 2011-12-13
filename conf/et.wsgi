import os
import sys
sys.stdout = sys.stderr
# Add the virtual Python environment site-packages directory to the path
import site
site.addsitedir('/home/build/elephanttalk/lib/python2.7/site-packages')


# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
import os
os.environ['PYTHON_EGG_CACHE'] = '/var/www/elephanttalk/egg-cache'

#If your project is not on your PYTHONPATH by default you can add the following
sys.path.append('/home/build/elephanttalk/src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
