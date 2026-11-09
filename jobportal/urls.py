"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from job import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.Register.as_view()),
    path('login',obtain_auth_token),
    path('create',views.create.as_view()),
    path('view',views.view.as_view()),
    path('retrive/<int:i>',views.retrive.as_view()),
    path('update/<int:i>',views.update.as_view()),
    path('delete/<int:i>',views.delete.as_view()),
    path('Logout',views.Logout.as_view()),
   


]
