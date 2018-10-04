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

    def getname(self):
        return self.firstname




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
    isavaliable = (('yes','yes') , ('no','no'))
    status = models.CharField(max_length = 10 , default = 'yes', choices=isavaliable)


#class reservation(models.Model):
