# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext

from forms import UserCreationForm, UserProfileForm
from models import UserProfile

from pdb import set_trace as st

def edit_user_profile(request):
    user = get_object_or_404(User, username=request.user.username)
    profile = user.get_profile()
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            profile.bio = form.cleaned_data['bio']
            profile.save()
            return redirect("/profile/%s/" % request.user.username)
        else:
            pass
    else:
        initial_data = {
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'email' : user.email,
            'bio' : profile.bio,
            }
        form = UserProfileForm(initial=initial_data)
    return render_to_response(
        'userprofile/edit_profile.html', 
        {'form': form},
        context_instance=RequestContext(request))
    

def get_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render_to_response(
        'userprofile/profile.html', 
        {'profile': user.get_profile()},
        context_instance=RequestContext(request))
    
    
def list_users(request):
    users = get_list_or_404(UserProfile)
    return render_to_response(
        'userprofile/user_list.html',
        {'users': users},
        context_instance=RequestContext(request))

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], 
                                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect("/")
        else:
            pass
    else:
        form = UserCreationForm()
    return render_to_response(
        'registration/register.html', 
        {'form': form},
        context_instance=RequestContext(request))
        