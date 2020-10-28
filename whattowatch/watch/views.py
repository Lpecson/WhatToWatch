from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

@login_required(login_url="/login/")
def blank(request):
    return redirect("/home/")

@login_required(login_url="/login/")
def home(request):
    return render(request,'home.html',{'name':'LineUp Login Signup'})

@login_required(login_url="/login/")
def profile_view(request):
    prof = models.Profile.objects.get(profile_user=request.user)
    welc = "Welcome to your profile page: "
    welc += prof.profile_fname + " " + prof.profile_lname
    if request.method == "POST":
        form = forms.BioForm(request.POST)
        if form.is_valid():
            prof.profile_bio = form.cleaned_data["profile_bio"]
            prof.save()
            form = forms.BioForm()
            return redirect('/profilePage/')
    else:
        form = forms.BioForm()
    context = {
        "body":welc,
        "form":form,
        "title":"Profile Page",
        "bio":prof.profile_bio,
        "profile_picture":prof.profile_image.url,
    }
    return render(request, "profile_page.html", context=context)

def login_view(request):
    # Authentication works
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home/')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'name':'LineUp login Signup','form':form})

@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect("/home/")

def signup(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
        "title":"Registering User",
        }
    return render(request, "signup.html", context=context)