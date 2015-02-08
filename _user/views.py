from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from forms import EmailUserCreationForm, UserForm
from models import *


def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EmailUserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def profile_update(request, profile_username):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_by_username', profile_username=request.user.username)
    elif request.user.username != profile_username:
        return redirect('profile')
    else:
        form = UserForm(instance=request.user)
    return render(request, "profile.html", {'form': form})


def profile_by_username(request, profile_username=""):
    if not profile_username:
        profile_username = request.user.username
    profile_user = User.objects.get(username=profile_username)
    return render(request, "profile_username.html", {'profile_user': profile_user})
