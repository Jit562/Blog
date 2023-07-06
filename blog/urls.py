"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from miniblog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('home/',PostListView.as_view(), name = 'home'),
    path('post/<int:pk>',PostDetailView.as_view(), name = 'post'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('signup/', Singup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', User_logout, name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('addpost/', AddPost, name='addpost'),
    path('/<int:id>/', EditPost, name='editpost'),
    path('delete/<int:id>/', Delete, name='delete'),
    path('changepass/', user_change_pass, name='changepass'),
    
]
