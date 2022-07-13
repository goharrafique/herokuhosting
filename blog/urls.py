from django.contrib import admin
from django.urls import path,include
# from icoder import views
from . import views
urlpatterns = [
    
    path('',views.blogHome,name='blogHome' ),
    path('<str:slug>/',views.blogPost,name='blogPost' ),
]