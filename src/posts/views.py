# Create your views here.

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render_to_response
from django.template import Context, RequestContext

from pdb import set_trace as st

from models import *

def index(request):
    # return all base classes and order them by name.
    posts = Post.objects.all()
    
    template = 'index.html'
    return render_to_response(
        template,
        {'posts':posts},
        context_instance=RequestContext(request))
        
def get_post(request, slug):
    post = Post.objects.get(slug=slug)
    st()
    template = 'posts/post.html'
    return render_to_response(
        template,
        {'post':post},
        context_instance=RequestContext(request))