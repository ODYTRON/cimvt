"""cimvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# import login logout views
from django.contrib.auth import views as auth_views
from django.urls import path, include
# import the view directly (the user register)
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
# this is not necessary because you have declared the home page of your app
# the system navigates from the first page. The first pattern only is ok
# when it match the first pattern then goes to the urls of the app and processes the remaining
# strings. IF YOU ACTIVATE CODE THIS BELOW YOU WILL HAVE PROBLEM WITH NAVIGATION
 # path('about/', include('blog.urls')),
]