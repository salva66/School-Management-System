import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from schoolapp.EmailBackEnd import EmailBackEnd

# Create your views here.
def ShowLoginPage(request):
    return render(request, 'login_page.html')

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user!=None:
            login(request, user)
            return HttpResponse("/admin_home")
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")