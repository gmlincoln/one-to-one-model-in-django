from django.shortcuts import render, redirect
from django.http import HttpResponse

def dashboardPage(req):

    return render(req, 'myAdmin/index.html')

def loginPage(req):

    return render(req, 'common/login.html')
    

def registerPage(req):

    return render(req, 'common/register.html')
    