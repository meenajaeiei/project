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
path('home/',views.mainhome, name = 'home'),
path('blog/', include('blog.urls', namespace='blog')),


#path('bookmarks/', include('bookmarks.urls')),
#path(r'', home_page),
#path(r'login/', user_login, name='login'),
# path('login/', auth_views.LoginView.as_view(), name='login'),
# path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#path('', views.dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
