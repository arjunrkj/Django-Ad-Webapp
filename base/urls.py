from django.urls import path
from . import views

urlpatterns = [
    path('logout/',views.logoutuser,name="logout"),
    path('register/',views.registeruser,name="register"),
    path('login/',views.loginPage,name="login"),
    path('',views.home,name="home"),
    path('post/<str:pk>/',views.post,name="post"),
    path('createpost/',views.createPost,name="createpost"),
    path('updatepost/<str:pk>',views.updatePost,name="updatepost"),
    path('deletepost/<str:pk>',views.deletePost,name="deletepost"),
    path('myposts/',views.myposts,name="myposts"),
    path('signup/',views.myposts,name="signup"),
]