from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Employee(models.Model):
    ROLE = (('student' , 'student') , ('staff' , 'staff') , ('teacher' , 'teacher') )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100 , default='name')
    lastname = models.CharField(max_length=100 , default = 'lastname')
    role = models.CharField(max_length=100 , default = 'Student', choices=ROLE)

    def getempid(self):
        return self.id

    def __str__(self):
        return self.user.username

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def get_absolute_url(self):
        return reverse('blog:post_detail',
        args=[self.publish.year,
        self.publish.month,
        self.publish.day,
        self.slug])


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class room(models.Model):
    roomname = models.CharField(max_length=100 , default = 'roomname')
    isavaliable = (('available','available') , ('unavailable','unavailable') , ('pending' , 'pending'), ('reserved', 'reserved'))
    status = models.CharField(max_length = 15 , default = 'available', choices=isavaliable)
    width = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    slug = models.SlugField(max_length=100 , default = 'roomname')
    svgpath = models.CharField(max_length = 3000 , default = "PATH")
    floor = models.IntegerField(default = 1)
    note = models.CharField(max_length = 10, default = "")

    def __str__(self):
        return self.roomname

class BookManager(models.Manager):

    def create_book(self, student ,  room ,begin_reserve , end_reserve , reason , teacher):
        reservation = self.create(
        student = student , #Employee.objects.get(username = "mhee") ,
        teacher = teacher , #Employee.objects.get(username = "mhee2") ,
        room = room , #room.objects.get(roomname = "M16"),
        status = "pending",
        duration_begin = begin_reserve,
        duration_end = end_reserve,
        day_of_reserve =  timezone.now(),
        reason_of_reserve = reason
        )
        # do something with the book
        return reservation


    def get_booklist(self , student_id):

        user_a = User.objects.get(username = student_id)
        emp = Employee.objects.get(user = user_a)
        reservation_list = reservation.objects.filter(student = emp)
        
        return reservation_list
    

        



class reservation(models.Model):
    student = models.ForeignKey(Employee, related_name = "student" , on_delete=models.CASCADE ,blank = True,null=True)
    
    teacher = models.ForeignKey(Employee, related_name = "teacher" , on_delete=models.CASCADE ,blank = True,null=True)
    reason_of_teacher = models.CharField(max_length = 300, default = "")
    teacher_approve_date = models.DateTimeField(default="1111-01-01 01:11")
    
    staff = models.ForeignKey(Employee, related_name = "staff" , on_delete=models.CASCADE ,blank = True,null=True)
    reason_of_staff = models.CharField(max_length = 300, default = "")
    staff_approve_date = models.DateTimeField(default="1111-01-01 01:11")
    
    room = models.ForeignKey(room , related_name = "room" , on_delete=models.CASCADE)
    status_list = (("pending" , "pending"), ("accepted" , "accepted"),  ("denied" , "denied") )
    reason_of_reserve = models.CharField(max_length = 300 , default = "reason" , blank = True)
    status = models.CharField(max_length = 20 , default = 'pending', choices=status_list)
    teacher_result = models.CharField(max_length = 20 , default = 'pending', choices=status_list)
    staff_result = models.CharField(max_length = 20 , default = 'pending', choices=status_list)
    day_of_reserve = models.DateTimeField(default=timezone.now)
    duration_begin =  models.DateTimeField(default=timezone.now)
    duration_end =  models.DateTimeField(default=timezone.now)
    objects = BookManager()

    def cancel_book(self):
        room_obj = self.room
        room_obj.status = "avaliable"
        room_obj.save()
        self.delete()
        print("hi")
