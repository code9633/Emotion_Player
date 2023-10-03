from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('predict/',views.predict_emotion, name = "predict"),
    # path('result/<str:emotion>/', views.result, name= 'result'),
    path('signup/', views.signupPage , name="signupPage"),
    path('login/', views.loginPage, name= "loginPage"),
    path('logout/', views.logout, name="logout"),
]
