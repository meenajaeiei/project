from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# @login_required
# def dashboard(request):
#     return render(request,'dashboard.html',{'section': 'dashboard'})
#
def home_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'blog/login.html', {})

def mainhome(request):
    return render(request, "blog/home.html" , {})
