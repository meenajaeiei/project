from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


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




# class Person(models.Model):
#     first_name = models.CharField(
#         max_length=140)
#     last_name = models.CharField(
#         max_length=140)
#     born = models.DateField()
#     died = models.DateField(null=True,
#                             blank=True)
#
#
#     class Meta:
#         ordering = (
#             'last_name', 'first_name')
#
#     def __str__(self):
#         if self.died:
#             return '{}, {} ({}-{})'.format(
#                 self.last_name,
#                 self.first_name,
#                 self.born,
#                 self.died)
#         return '{}, {} ({})'.format(
#                 self.last_name,
#                 self.first_name,
#                 self.born)


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
    #roomid = models.AutoField()
    roomname = models.CharField(max_length=100 , default = 'roomname')
    isavaliable = (('yes','yes') , ('no','no') , ('pending' , 'pending'))
    status = models.CharField(max_length = 10 , default = 'yes', choices=isavaliable)
    width = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    slug = models.SlugField(max_length=100 , default = 'roomname')
    svgpath = models.CharField(max_length = 3000 , default = "PATH")
    floor = models.IntegerField(default = 1)

    def __str__(self):
        return self.roomname

class BookManager(models.Manager):
    def create_book(self, student ,  room ,begin_reserve , end_reserve):
        reservation = self.create(
        student = student , #Employee.objects.get(username = "mhee") ,
        #teacher = teacher , #Employee.objects.get(username = "mhee2") ,
        room = room , #room.objects.get(roomname = "M16"),
        status = "pending",
        duration_begin = begin_reserve,
        duration_end = end_reserve,
        day_of_reserve =  timezone.now()
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
    staff = models.ForeignKey(Employee, related_name = "staff" , on_delete=models.CASCADE ,blank = True,null=True)
    # staff = models.CharField(max_length=100, default="-")
    
    room = models.ForeignKey(room , related_name = "room" , on_delete=models.CASCADE)
    status_list = (("pending" , "pending"), ("accepted" , "accepted"),  ("denied" , "denied") )
    reason_of_reserve = models.CharField(max_length = 300 , default = "reason")
    status = models.CharField(max_length = 20 , default = 'pending', choices=status_list)

    teacher_result = models.CharField(max_length = 20 , default = 'pending', choices=status_list)
    staff_result = models.CharField(max_length = 20 , default = 'pending', choices=status_list)
    
    day_of_reserve = models.DateTimeField(default=timezone.now)
    duration_begin =  models.DateTimeField(default=timezone.now)
    duration_end =  models.DateTimeField(default=timezone.now)
    objects = BookManager()

    # def __str__(self):
    #     return str(self.id)

    def cancel_book(self):
        room_obj = self.room
        room_obj.status = "yes"
        room_obj.save()
        self.delete()
        print("hi")
