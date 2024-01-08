from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path("expression", views.expression, name = "expression" ),
    path('userLogin/', views.userLogin, name = "login"),
    path('userRegister/', views.userRegistration, name = "register"),
    path('logout/', auth_views.LogoutView.as_view(), name= "logout"),
    path('social-auth/', include('social_django.urls', namespace='social') ),
    path('get_music_details/',views.get_music_details, name = 'get_music_details' ),
    
]
 
