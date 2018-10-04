from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from blog.models import *

@login_required
def changepass(request):
     return render(request, 'blog/password_change_form.html', {})



def home_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            dict = {'Name': username}
            return render(request, 'blog/home.html' , {"dict":dict})
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'blog/login.html', {})

def mainhome(request):
    return render(request, "blog/home.html" , {})
