from django.urls import path
from . import views

urlpatterns = [
    path('', views.recognition, name="Home"),
    path('about/', views.about, name="AboutUs"),
    path('login/', views.login, name="Login"),
    path('logout/', views.logout, name="Logout"),
    path('profile/', views.profile, name="profile"),
    path('attendance/', views.attendance, name="attendance"),
    path('graphs/', views.graphs, name="graphs"),
    path('cpassword/', views.cpassword, name="cpassword"),
    path('change/', views.change, name="change"),
    path('notification/', views.notification, name="notification"),
] 