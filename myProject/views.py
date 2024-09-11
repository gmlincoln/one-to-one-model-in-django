from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required




@login_required
def dashboardPage(req):

    return render(req, 'myAdmin/index.html')
    

def registerPage(req):

    return render(req, 'common/register.html')

def loginPage(req):

    if req.method == 'POST':

        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)
        
        if user:
            login(req, user)
            return redirect('dashboardPage')
        else:
            return HttpResponse('Sorry! username or password not matched!')


    return render(req, 'common/login.html')

def logoutPage(req):

    logout(req)

    return redirect('loginPage')
    