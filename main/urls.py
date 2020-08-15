from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name="Homepage"),
    path('login/',views.discordlogin, name="Login with discord"),
    path('rddd/',views.rddd, name="REMOTE DD"),
    path('rdd/',views.rdd, name="REMOTE DD"),
    path('logout/', views.logout, name="Logout of site"),
    path('logintest/', views.discordtest, name="Return the username to test if the user is logged in"),
    path('login/',views.discordlogin, name="Login with discord"),
    path('connected/',views.connected, name="Return Home"),
    path('connection/',views.connected, name="Return Home"),
]
