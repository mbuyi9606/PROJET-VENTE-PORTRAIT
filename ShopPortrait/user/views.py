from django.shortcuts import render, redirect
from user.models import User
from user.forms import SingupForm
from django.contrib.auth import login, authenticate

# Create your views here.

def login(request):

    login = request.GET.get('login')
    password = request.GET.get('password')
    if request.method == 'POST':
        user = authenticate(username=login, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        
        else:
            redirect('/')
        
    return render(request, 'user/login.html')

def Singup(request):

    form = SingupForm(request.POST)
    if request.method == 'POST':
        pass