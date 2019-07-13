"""solo URL Configuration

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
from django.urls import path , include
from signup import view as signup_view
from .view import user_db ,index_page ,home_page ,user_cp,user_vib ,user_sbr ,vaab_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page , name="home"),
    path('', include('django.contrib.auth.urls')),
    path('Dashboard/',user_db),
    path('ChangePassword/',user_cp , name='change_password'),
    path('view_issued_books/',user_vib),
    path('view_all_archive_books/',vaab_view),
    path('submit_book_request/',user_sbr),
    path('signup/', signup_view.signup, name='signup'),
]
