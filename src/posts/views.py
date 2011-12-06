# Create your views here.

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext

from pdb import set_trace as st

from models import *
from forms import PostForm

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
    template = 'posts/post.html'
    return render_to_response(
        template,
        {'post':post},
        context_instance=RequestContext(request))
        
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            s = form.cleaned_data['title']
            i = s.split(" ")
            slug = "-".join(i)
            post = Post(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                slug = slug,
            )
            post.save()
            return redirect("/%s" % post.slug)
        else:
            # form validation did not go so well.
            pass
    else:
        # assuming GET
        form = PostForm()
    return render_to_response(
        'posts/addpost.html', 
        {'form': form},
        context_instance=RequestContext(request))