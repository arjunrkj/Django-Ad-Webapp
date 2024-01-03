from django.urls import path
from . import views

urlpatterns = [
    path('logout/',views.logoutuser,name="logout"),
    path('register/',views.registeruser,name="register"),
    path('login/',views.loginPage,name="login"),
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('createroom/',views.createRoom,name="createroom"),
    path('updateroom/<str:pk>',views.updateRoom,name="updateroom"),
    path('deleteroom/<str:pk>',views.deleteRoom,name="deleteroom"),
    path('myposts/',views.myposts,name="myposts"),
    path('signup/',views.myposts,name="signup"),
]