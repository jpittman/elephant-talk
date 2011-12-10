# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext

from forms import UserCreationForm

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
        