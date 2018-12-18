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

def dev_view(request):
    return render(request , "blog/home.html" , {})

#Post.objects.filter

def isRoomExpire():
    res = reservation.objects.all() #ดูว่าreservationอันไหนหมดอายุ
    for i in res:
        if timezone.now()  > i.duration_end and (i.status == "pending" or i.status == "accepted"):
            i.room.status = "avaliable"
            i.room.save()
            i.delete()
            print(" reservation was expired on isRoomExpire function")
    
    res = reservation.objects.all() #ถ้าreservationถูกอนุมัติห้องต้องเป็นสถานะ reserved
    for z in res:
        if(z.status == 'accepted'):
            print("some reservation was accepted")
            z.room.status = "reserved"
            z.room.save()
    
    res = reservation.objects.all()
    for x in res:
        if(x.room.status == 'reserved' and x.status == 'pending'):
            print("room was reserved , your reservation was set to denied automatically.")
            x.status = "denied"
            x.save()
        
    
             
USER_LOGGED = ""
PASS_LOGGED = ""

def show_table(request):
    res_list = []
    res = reservation.objects.all()
    for i in res:
        if(i.status == "pending" or i.status == "accepted"):
            res_list.append(i)
    return render(request, 'blog/reservation_table.html', {'res_list' : res_list, "emp" : Employee.objects.get(user = User.objects.get(username = request.session['username'])) })



def home_page(request):
    if request.method == 'POST' and 'password' in request.POST:
        global USER_LOGGED
        global PASS_LOGGED 
        USER_LOGGED = request.POST['username']
        PASS_LOGGED = request.POST['password']

        usernamex = USER_LOGGED
        password = PASS_LOGGED
        user = authenticate(request, username=usernamex, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            emp_id = User.objects.get(username = usernamex)
            emp = Employee.objects.get(user = emp_id) #(id = emp_id.id)
            request.session['username'] = usernamex
            destination = "blog/home.html"
            
            context = {}
            return render(request , destination  , context)

            #สำหรับเข้าหน้าแรกมาเด้งไปหน้าการจองเลย
            # return render(request , "blog/reservation_map_1.html" , {"teachers" : Employee.objects.filter(role = "teacher"),"emp" : Employee.objects.get(user = User.objects.get(username = request.session['username'])) ,
            #                                                     "rooms" : room.objects.all()})
        else:
            return render(request, 'blog/error.html', {})
    else:
        print("please login first")
        return render(request, 'blog/login_2.html', {})



def mainhome(request):
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
            o_room.save()
    return render(request , 'blog/reservation_room.html' , {'rooms' : rooms})

def test(request):
    return render(request, "blog/test.html" , {"range" : range(0, 100 , 1)})


def strtodate(strtime):
    ans = datetime(int(strtime[0:4]) , int(strtime[5:7]) , int(strtime[8:10]) , int(strtime[10:12]) , int(strtime[13:15]))
    return ans

def reserve_room(STDusername , roomarg , period_s , period_n , reason, teacher): #period_s = beginreservation , period_n = endreservation 
    user_obj = User.objects.get(username = STDusername)
    teacher_obj = User.objects.get(username = teacher)
    emp_obj = Employee.objects.get(user = user_obj)
    room_obj = room.objects.get(roomname = roomarg)
    teacher_obj = Employee.objects.get(user = User.objects.get(username = teacher))
    room_obj.status = "pending" #ตั้งสถานะห้องเป็นpending
    reservation.objects.create_book(emp_obj , room_obj , period_s , period_n , reason, teacher_obj)  #def create_book(self, student ,  room ,begin_reserve , end_reserve):
    room_obj.save()


def showmap_1(request):
    isRoomExpire()
    global USER_LOGGED
    print("USER_LOGGED" + USER_LOGGED)
    print(request.session['username'])
    if 'res-date-start' in request.POST and 'res-time-start' in request.POST and 'res-date-end' in request.POST and 'res-time-end' in request.POST and 'username' in request.POST and 'room' in request.POST :

        reserve_room(request.POST["username"] , request.POST['room'] , strtodate(request.POST['res-date-start']+request.POST['res-time-start']) , strtodate(request.POST['res-date-end']+request.POST['res-time-end']) , request.POST['reason'], request.POST['teacher'] )
        return render(request, "blog/status.html" , {"reservation_list": reservation.objects.get_booklist(User.objects.get(username = request.session['username']))}  )
    
    r_check = []
    #กดเช็ค
    if 'check-date-start' in request.GET and 'check-date-end' in request.GET:
        start_time = strtodate(request.GET['check-date-start']+request.GET['check-time-start']).replace(tzinfo = pytz.UTC)
        end_time =   strtodate(request.GET['check-date-end']+request.GET['check-time-end']).replace(tzinfo = pytz.UTC)
        cc = reservation.objects.all()
        for r_obj in  cc:
            if(r_obj.duration_begin > start_time and r_obj.duration_begin < end_time and r_obj.status != 'denied'):
                r_check.append(r_obj)
        
        return render(request , "blog/reservation_map_1.html" , 
        {

        "teachers" : Employee.objects.filter(role = "teacher"),
        "end_time" : end_time ,
        "start_time":start_time,
        "rooms" :  room.objects.all() , 
        "r_check": r_check })
    try:
        return render(request , "blog/reservation_map_1.html" , {"teachers" : Employee.objects.filter(role = "teacher"),"emp" : Employee.objects.get(user = User.objects.get(username = request.session['username'])) ,
                                                                "rooms" : room.objects.all()})
    except Exception as e:
        return render(request , "blog/reservation_map_1.html" , {"rooms" : room.objects.all()})

def managereservation(request):
    u = request.session['username']
    staff_obj = Employee.objects.get(user = User.objects.get(username = u)) #get user object teacher/staff
    if 'accepted' in request.POST or 'denied' in request.POST:
        action = 'accepted' if 'accepted' in request.POST else 'denied'
        reserve_id = int(request.POST['resno']) #reservation id
        reserve = reservation.objects.get(id = reserve_id) #get reservation object that user selected
        reason = request.POST['reason']
        actionReserve(action, reserve, staff_obj, reason)

    temp_role = str (Employee.objects.get(user = User.objects.get(username = u)).role)
    if (temp_role == 'teacher' or temp_role == 'staff'):
        if temp_role == 'teacher':    
            return render(request , "blog/reservation_manage.html",  {"emp":staff_obj, 
            "res": reservation.objects.filter(status = "pending") and reservation.objects.filter(teacher = staff_obj)})
        if temp_role == 'staff':
            return render(request , "blog/reservation_manage.html",  {"emp":staff_obj, "res": reservation.objects.filter(status = "pending")})
    else:
        return render(request, "blog/home.html" , {})

def manage_room(request):
    if 'roomname' in request.GET:
        selected_room = room.objects.get(roomname = request.GET['roomname'])
        if 'roomstatus' in request.GET:
            selected_room.status = request.GET['roomstatus']
        if request.GET["note"] != "":
            selected_room.note = request.GET["note"]
        selected_room.save()        
    return render(request, "blog/manage_room.html", {"room":room.objects.all(), "emp" : Employee.objects.get(user = User.objects.get(username = request.session['username']))})


#addition Function
def getreservation(request):
    if "reservation" in request.GET and "reservation" in request.GET:
        res_obj = reservation.objects.get(id = int(request.GET['resno']) )
        res_obj.cancel_book()
    reservation_list = reservation.objects.get_booklist(User.objects.get(username = request.session['username']))
    return render(request, "blog/status.html" , {"reservation_list":reservation_list})


def actionReserve(action, reserve, staff_obj, reason):

    role = staff_obj.role
    if role == "staff":
        reserve.staff_result = action
        reserve.staff = staff_obj
        reserve.reason_of_staff = reason
        reserve.staff_approve_date = datetime.now()
    elif role == "teacher":
        reserve.teacher_result = action
        reserve.reason_of_teacher = reason
        print(datetime.now())
        reserve.teacher_approve_date = datetime.now()
    
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
