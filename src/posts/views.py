# Create your views here.

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext


from pdb import set_trace as st

from models import *
from forms import PostForm, UserForm

# helper functions

def not_staff_or_superuser(user):
    if user:
        if user.is_staff or user.is_superuser:
            return True
    return False

# views

def index(request):
    # return all base classes and order them by name.
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    # If page request (9999) is out of range, deliver last page of results.
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    
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

@login_required
@user_passes_test(not_staff_or_superuser, login_url='/')
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
                user = request.user,
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

