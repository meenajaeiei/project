from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login , logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from blog.models import room , Employee , User , reservation
from django.contrib import messages
from datetime import datetime
import pytz

@login_required
def changepass(request):
     return render(request, 'blog/password_change_form.html', {})

def logout_view(request):
    logout(request)
    return render(request , "blog/logout.html" , {})

#Post.objects.filter

def home_page(request):
    if request.method == 'POST':
        print("login")
        usernamex = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usernamex, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            emp_id = User.objects.get(username = usernamex)
            emp = Employee.objects.get(id = emp_id.id)
            request.session['username'] = usernamex 


            return render(request, 'blog/home.html' , {"emp":emp})
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('Invalid login')
    else:
        return render(request, 'blog/login.html', {})

def mainhome(request):

    # context = {
    # "student":"student"
    # }
    #return render(request, "blog/home.html" , {context})
    return render(request, "blog/home.html" , {})




def room_detail(request):
    rooms = room.objects.all()
    if 'room' in request.GET and 'username' in request.GET:

        print(request.GET['room'])
        o_room = room.objects.get(roomname = request.GET['room']) #ดึงค่าสถานะห้อง\
        user_obj = User.objects.get(username = request.GET['username'])
        user_obj = Employee.objects.get(id = user_obj.id)

        
        
        if(o_room.status  == "pending"):
            print("anti - double transaction")
        else:
            o_room.status = "pending" #ตั้งสถานะห้องเป็นpending
            #reservation.objects.create_book(user_obj , o_room)
            o_room.save()



    else:
        print("ihere")



    return render(request , 'blog/reservation_room.html' , {'rooms' : rooms})

def test(request):
    return render(request, "blog/test.html" , {"range" : range(0, 100 , 1)})


def strtodate(strtime):
    ans = datetime(int(strtime[0:4]) , int(strtime[5:7]) , int(strtime[8:10]) , int(strtime[11:13]) , int(strtime[14:17]))
    return ans

def reserve_room(STDusername , roomarg , period_s , period_n): #period_s = beginreservation , period_n = endreservation 
    user_obj = User.objects.get(username = STDusername)
    emp_obj = Employee.objects.get(id = user_obj.id)
    room_obj = room.objects.get(roomname = roomarg)
    if(room_obj.status  == "pending"):
        print("anti - double transaction")
    else:
        room_obj.status = "pending" #ตั้งสถานะห้องเป็นpending
        reservation.objects.create_book(emp_obj , room_obj , period_s , period_n)  #def create_book(self, student ,  room ,begin_reserve , end_reserve):
        room_obj.save()



def showmap_1(request):
    
    if 'beginreservation' in request.GET and 'username' in request.GET and 'room' in request.GET and 'endreservation' in request.GET:
        reserve_room(request.GET["username"] , request.GET['room'] , strtodate(request.GET['beginreservation']) , strtodate(request.GET['endreservation']) )
        # o_room = room.objects.get(roomname = request.GET['room']) #ดึงค่าสถานะห้อง\
        # user_obj = User.objects.get(username = request.GET['username'])
        # user_obj = Employee.objects.get(id = user_obj.id)

        # if(o_room.status  == "pending"):
        #     print("anti - double transaction")
        # else:
        #     o_room.status = "pending" #ตั้งสถานะห้องเป็นpending
        #     reservation.objects.create_book(user_obj , o_room , strtodate(request.GET['beginreservation']) , strtodate(request.GET['endreservation'])) 
        #     #def create_book(self, student ,  room ,begin_reserve , end_reserve):
        #     o_room.save()
    
    r_check = []
    if 'start_time' in request.GET and 'end_time' in request.GET:
        start_time = strtodate(request.GET["start_time"]).replace(tzinfo = pytz.UTC)
        end_time = strtodate(request.GET["end_time"]).replace(tzinfo = pytz.UTC)
        #datetime.datetime.now().strftime("%y-%m-%d--%H:%M")
        for r_obj in reservation.objects.all():
            print("we_rent on" , r_obj.duration_begin , "|| you finding start " , start_time , " end" ,end_time)
            if(r_obj.duration_begin > start_time and r_obj.duration_begin < end_time and r_obj.room.floor == 1):
                r_check.append(r_obj.room)
        
        print(r_check)

        return render(request , "blog/reservation_map_1.html" , 
        {"end_time" : end_time ,
        "start_time":start_time,
        "rooms" : room.objects.filter(floor=1) , 
        "r_check": r_check })

    return render(request , "blog/reservation_map_1.html" , {"rooms" : room.objects.filter(floor=1)})


def showmap_2(request):
    if 'beginreservation' in request.GET and 'username' in request.GET and 'room' in request.GET and 'endreservation' in request.GET:
        reserve_room(request.GET["username"] , request.GET['room'] , request.GET['beginreservation'] , request.GET['endreservation'] )
    
    return render(request , "blog/reservation_map_2.html" , {"rooms" : room.objects.filter(floor=2)})

def showmap_3(request):
    if 'beginreservation' in request.GET and 'username' in request.GET and 'room' in request.GET and 'endreservation' in request.GET:
        reserve_room(request.GET["username"] , request.GET['room'] , request.GET['beginreservation'] , request.GET['endreservation'] )
    
    return render(request , "blog/reservation_map_3.html" , {"rooms" : room.objects.filter(floor=3)})




def managereservation(request):

    temp_role = str (Employee.objects.get(id = User.objects.get(username = request.session['username']).id).role)

    ei1 = "teacher"
    ei2 = "staff"
    if (temp_role == ei1 or temp_role == ei2 ):

        
        return render(request , "blog/reservation_manage.html",  {"res": reservation.objects.filter(status = "pending")} )
    else:
        return render(request, "blog/home.html" , {})


def getreservation(request):
    if "reservation" in request.GET:
        res_obj = reservation.objects.get(id = int(request.GET['reservation']) )
        res_obj.cancel_book()
    reservation_list = reservation.objects.get_booklist(User.objects.get(username = request.session['username'] ))
    return render(request, "blog/reservation_status.html" , {"reservation_list":reservation_list})
