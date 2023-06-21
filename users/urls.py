from django.urls import path
from . import views 
urlpatterns=[
    path('login/',views.loginUser,name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('account/',views.userAccount,name="account"),
    path('',views.profiles,name="profiles"),
    path('edit-account/',views.editAccount,name="edit-account"),
    path('profile/<str:pk>/',views.userProfile,name="user-profile"),
]