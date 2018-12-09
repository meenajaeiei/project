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
    path('', views.showmap_1, name = 'home'),
    path('logout/', views.logout_view, name='logout'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('test/', views.test, name='test'),
    path('password_change/', views.changepass, name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reservation_room/' , views.room_detail , name= 'reservation_room'),
    path('reservation_status/' , views.getreservation , name= 'reservation_status'),
    path('reservation_manage/' , views.managereservation , name = "reservation_manage"), 
    path('reservation_map_1/', views.showmap_1 , name = "reservation_map_1"),
    path('manage_room', views.manage_room , name="manage_room")
  # path('reservation_map_2/', views.showmap_2 , name = "reservation_map_2"),
  # path('reservation_map_3/', views.showmap_3 , name = "reservation_map_3"),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
