from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('signup/', views.signupPage , name="signupPage"),
    path('login/', views.loginPage, name= "loginPage"),
    path('logout/', views.logout, name="logout"),
]
