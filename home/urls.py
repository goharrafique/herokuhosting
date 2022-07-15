from django.contrib import admin
from django.urls import path,include
# from icoder import views
from home import views
urlpatterns = [
    
    path('',views.home,name='home' ),
    path('contact',views.contact,name='contact' ),
    path('about',views.about,name='about' ),
    path('home',views.home,name='home' ),
    path('search',views.search,name='search' ),
    path('signup',views.handleSign,name='handleSign' ),
    path('login',views.handleLogin,name='handleLogin' ),
    path('logout',views.handleLogout,name='handleLogout' )
]