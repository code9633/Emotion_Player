from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('get_emotion/',views.get_emotion, name = "get_emotion"),
    path('signup/', views.signupPage , name="signupPage"),
    path('login/', views.loginPage, name= "loginPage"),
    path('logout/', views.logout, name="logout"),
]
