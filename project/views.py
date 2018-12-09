from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login , logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from blog.models import room , Employee , User , reservation
from django.contrib import messages
from datetime import datetime
import pytz
from django.utils import timezone


@login_required
def changepass(request):
     return render(request, 'blog/password_change_form.html', {})

def logout_view(request):
    logout(request)
    return render(request , "blog/logout_2.html" , {})

#Post.objects.filter

def isRoomExpire():
    res = reservation.objects.filter(status="accepted")
    for i in res:
        if timezone.now()  > i.duration_end:
            i.room.status = "available"
            i.save()
            i.delete()
    
             
USER_LOGGED = ""
PASS_LOGGED = ""
def home_page(request):
    if request.method == 'POST' and 'password' in request.POST:
        global USER_LOGGED
        global PASS_LOGGED 
        USER_LOGGED = request.POST['username']
        PASS_LOGGED = request.POST['password']

        usernamex = USER_LOGGED
        password = PASS_LOGGED
        user = authenticate(request, username=usernamex, password=password)
        print(usernamex)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            emp_id = User.objects.get(username = usernamex)
            emp = Employee.objects.get(user = emp_id) #(id = emp_id.id)
            request.session['username'] = usernamex
            destination = "blog/home.html"
            
            context = {}
            return render(request , destination  , context) 
            # if emp.role == "student": 
            #     return render(request, 'blog/reservation_map_1.html' , {"emp":emp , "rooms" : room.objects.all() })
            # elif emp.role == "staff" or emp.role == "teacher":
            #     return render(request , "blog/reservation_manage.html",  {"emp":emp ,"res": reservation.objects.filter(status = "pending")} )
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('Invalid login')
    else:
        print("please login first")
        return render(request, 'blog/login_2.html', {})

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




    return render(request , 'blog/reservation_room.html' , {'rooms' : rooms})

def test(request):
    return render(request, "blog/test.html" , {"range" : range(0, 100 , 1)})


def strtodate(strtime):
    ans = datetime(int(strtime[0:4]) , int(strtime[5:7]) , int(strtime[8:10]) , int(strtime[10:12]) , int(strtime[13:15]))
    return ans

def reserve_room(STDusername , roomarg , period_s , period_n , reason): #period_s = beginreservation , period_n = endreservation 
    user_obj = User.objects.get(username = STDusername)
    emp_obj = Employee.objects.get(user = user_obj)
    room_obj = room.objects.get(roomname = roomarg)
    if(room_obj.status  == "pending"):
        print("anti - double transaction")
    else:
        room_obj.status = "pending" #ตั้งสถานะห้องเป็นpending
        reservation.objects.create_book(emp_obj , room_obj , period_s , period_n , reason)  #def create_book(self, student ,  room ,begin_reserve , end_reserve):
        room_obj.save()


def showmap_1(request):
    isRoomExpire()
    global USER_LOGGED
    print("USER_LOGGED" + USER_LOGGED)
    if 'res-date-start' in request.POST and 'res-time-start' in request.POST and 'res-date-end' in request.POST and 'res-time-end' in request.POST and 'username' in request.POST and 'room' in request.POST :

        reserve_room(request.POST["username"] , request.POST['room'] , strtodate(request.POST['res-date-start']+request.POST['res-time-start']) , strtodate(request.POST['res-date-end']+request.POST['res-time-end']) , request.POST['reason'] )
        return render(request, "blog/status.html" , {"reservation_list": reservation.objects.get_booklist(User.objects.get(username = request.session['username']))}  )
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
    if 'check-date-start' in request.GET and 'check-date-end' in request.GET:
        start_time = strtodate(request.GET['check-date-start']+request.GET['check-time-start']).replace(tzinfo = pytz.UTC)
        end_time =   strtodate(request.GET['check-date-end']+request.GET['check-time-end']).replace(tzinfo = pytz.UTC)
        #datetime.datetime.now().strftime("%y-%m-%d--%H:%M")
        cc = reservation.objects.all()
        for r_obj in  cc:
            if(r_obj.duration_begin > start_time and r_obj.duration_begin < end_time and r_obj.status != 'denied'):
                r_check.append(r_obj.room)
        
        return render(request , "blog/reservation_map_1.html" , 
        {
        "end_time" : end_time ,
        "start_time":start_time,
        "rooms" :  room.objects.all() , 
        "r_check": r_check })
    try:
        return render(request , "blog/reservation_map_1.html" , {"emp" :  Employee.objects.get(user = User.objects.get(username = request.session['username'])) ,"rooms" : room.objects.all()})
    except Exception as e:
        return render(request , "blog/reservation_map_1.html" , {"rooms" : room.objects.all()})


# def showmap_2(request):
#     if 'beginreservation' in request.GET and 'username' in request.GET and 'room' in request.GET and 'endreservation' in request.GET:
#         reserve_room(request.GET["username"] , request.GET['room'] , request.GET['beginreservation'] , request.GET['endreservation'] )
    
#     return render(request , "blog/reservation_map_2.html" , {"rooms" : room.objects.filter(floor=2)})


# def showmap_3(request):
#     if 'res-date-start' in request.GET and 'res-time-start' in request.GET and 'res-date-end' in request.GET and 'res-time-end' in request.GET and 'username' in request.GET and 'room' in request.GET :
#         reserve_room(request.GET["username"] , request.GET['room'] , strtodate(request.GET['res-date-start']+request.GET['res-time-start']) , strtodate(request.GET['res-date-end']+request.GET['res-time-end']) )
#     r_check = []
#     if 'check-date-start' in request.GET and 'check-date-end' in request.GET:
#         start_time = strtodate(request.GET['check-date-start']+request.GET['check-time-start']).replace(tzinfo = pytz.UTC)
#         end_time =   strtodate(request.GET['check-date-end']+request.GET['check-time-end']).replace(tzinfo = pytz.UTC)
#         #datetime.datetime.now().strftime("%y-%m-%d--%H:%M")
#         for r_obj in reservation.objects.all():
#             print("we_rent on" , r_obj.duration_begin , "|| you finding start " , start_time , " end" ,end_time)
#             if(r_obj.duration_begin > start_time and r_obj.duration_begin < end_time and r_obj.room.floor == 3):
#                 r_check.append(r_obj.room)
        

#         return render(request , "blog/reservation_map_3.html" , 
#         {"end_time" : end_time ,
#         "start_time":start_time,
#         "rooms" : room.objects.filter(floor=3) , 
#         "r_check": r_check })

#     return render(request , "blog/reservation_map_3.html" , {"rooms" : room.objects.filter(floor=3)})


def managereservation(request):
    
    u = request.session['username']
    staff_obj = Employee.objects.get(user = User.objects.get(username = u)) #get user object teacher/staff

    if 'accepted' in request.POST or 'denied' in request.POST:
        action = 'accepted' if 'accepted' in request.POST else 'denied'
        print(action)
        reserve_id = int(request.POST['resno']) #reservation id
        # print(reserve_id)
        reserve = reservation.objects.get(id = reserve_id) #get reservation object that user selected
        actionReserve(action, reserve, staff_obj)

    temp_role = str (Employee.objects.get(user = User.objects.get(username = u)).role)
    if (temp_role == 'teacher' or temp_role == 'staff'):        
        return render(request , "blog/reservation_manage.html",  {"emp":staff_obj, "res": reservation.objects.filter(status = "pending")} )
    else:
        return render(request, "blog/home.html" , {})
    

def getreservation(request):
    if "reservation" in request.GET:
        res_obj = reservation.objects.get(id = int(request.GET['resno']) )
        res_obj.cancel_book()
    reservation_list = reservation.objects.get_booklist(User.objects.get(username = request.session['username']))
    return render(request, "blog/status.html" , {"reservation_list":reservation_list})


def actionReserve(action, reserve, staff_obj):

    role = staff_obj.role
    if role == "staff":
        reserve.staff_result = action
        reserve.staff = staff_obj
    elif role == "teacher":
        reserve.teacher_result = action
        reserve.teacher = staff_obj
    
    if reserve.staff_result  == 'denied' or reserve.teacher_result == 'denied':
        reserve.status = 'denied'
        room = reserve.room
        room.status = "available"
        room.save()
    if reserve.staff_result  == 'accepted' and reserve.teacher_result == 'accepted':
        reserve.status = 'accepted'
        room = reserve.room
        room.status = "pending"
        room.save()
    reserve.save()

def manage_room(request):
    print("LOL")
