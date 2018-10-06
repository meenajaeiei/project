from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login , logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from blog.models import room , Employee , User

@login_required
def changepass(request):
     return render(request, 'blog/password_change_form.html', {})

def logout_view(request):
    logout(request)
    return render(request , "blog/logout.html" , {})

#Post.objects.filter

def home_page(request):
    if request.method == 'POST':
        usernamex = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usernamex, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            emp_id = User.objects.get(username = usernamex)
            emp = Employee.objects.get(id = emp_id.id)
            return render(request, 'blog/home.html' , {'emp' : emp})
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'blog/login.html', {})

def mainhome(request):

    context = {
    "student":"student"
    }
    return render(request, "blog/home.html" , context)

def room_detail(request):
    rooms = room.q.all()
    return render(request , 'blog/rentroom.html' , {'rooms' : rooms})

def test(request):
    return render(request, "blog/test.html" , {})
