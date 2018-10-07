"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from .views import home_page,user_login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views




urlpatterns = [
path('admin/', admin.site.urls),
path('login/',views.home_page, name = 'login'),
path('',views.mainhome, name = 'home'),
path('logout/', views.logout_view, name='logout'),
path('blog/', include('blog.urls', namespace='blog')),
path('test/', views.test, name='test'),

path('password_change/',
views.changepass,
name='password_change'),

path('password_change/done/',
auth_views.PasswordChangeDoneView.as_view(),
name='password_change_done'),

path('reservation_room/' , views.room_detail , name= 'reservation_room'),
path('reservation_status/' , views.getreservation , name= 'reservation_status'),
#path('reservation_room/<slug:roomname>/' , views.getreservation , name = "xxx") ,

]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
