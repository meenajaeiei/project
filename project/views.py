from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login , logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from blog.models import room , Employee , User , reservation
from django.contrib import messages
from datetime import datetime


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
        print(usernamex)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            emp_id = User.objects.get(username = usernamex)
            emp = Employee.objects.get(user = emp_id) #(id = emp_id.id)
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
        reserve_room(request.GET["username"] , request.GET['room'] , request.GET['beginreservation'] , request.GET['endreservation'] )
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
    u = request.session['username']
    staff_obj = Employee.objects.get(user = User.objects.get(username = u)) #get user object teacher/staff

    if 'accepted' in request.GET or 'denied' in request.GET:
        action = 'accepted' if 'accepted' in request.GET else 'denied'
        # print(action)
        reserve_id = int(request.GET[action]) #reservation id
        # print(reserve_id)
        reserve = reservation.objects.get(id = reserve_id) #get reservation object that user selected
        actionReserve(action, reserve, staff_obj)

    temp_role = str (Employee.objects.get(user = User.objects.get(username = u)).role)
    if (temp_role == 'teacher' or temp_role == 'staff'):        
        return render(request , "blog/reservation_manage.html",  {"res": reservation.objects.filter(status = "pending") | reservation.objects.filter(status = "accepted-pending") | 
                                                                        reservation.objects.filter(status = "denied-pending")} )
    else:
        return render(request, "blog/home.html" , {})
    

def getreservation(request):
    if "reservation" in request.GET:
        res_obj = reservation.objects.get(id = int(request.GET['reservation']) )
        res_obj.cancel_book()
    reservation_list = reservation.objects.get_booklist(User.objects.get(username = request.session['username'] ))
    return render(request, "blog/reservation_status.html" , {"reservation_list":reservation_list})


def actionReserve(action, reserve, staff_obj):
    role = staff_obj.role
    if reserve.status == 'pending':
        if action == 'accepted':
            reserve.status = 'accepted-pending'
        elif action == 'denied':
            reserve.status = 'denied-pending'
        addWhoDoAction(role, staff_obj, reserve)

    elif reserve.status == 'accepted-pending':
        if (reserve.staff is None and role == 'staff') or (reserve.teacher is None and role == 'teacher'):
            if action == 'accepted':
                reserve.status = 'accepted'
            elif action == 'denied':
                reserve.status = 'denied'
            addWhoDoAction(role, staff_obj, reserve)
    elif reserve.status == 'denied-pending':
        if (reserve.staff is None and role == 'staff') or (reserve.teacher is None and role == 'teacher'):
            reserve.status = 'denied'
            addWhoDoAction(role, staff_obj, reserve)

def addWhoDoAction(role, staff_obj, reserve):
    if role == 'staff':
        reserve.staff = staff_obj
    elif role == 'teacher':
        reserve.teacher = staff_obj
    reserve.save()