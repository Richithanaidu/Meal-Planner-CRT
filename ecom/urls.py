"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1.views import layout,login,recipe,reg,doregister,logincheck,contact,userhome,adminhome,viewuser,modify,terms,pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',layout),
    path('login.html',login),
    path('recipe.html',recipe),
    path('register.html',reg),
    path('doregister/',doregister),
    path('logincheck',logincheck),
    path('contact.html',contact),
    path('userhome',userhome),
    path('adminhome',adminhome),
    path('viewuser.html',viewuser),
    path('modify',modify),
    path('terms.html',terms),
    path('pdf.html',pdf)
 ]
