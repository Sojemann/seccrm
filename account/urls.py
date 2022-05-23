from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"), 
        name='reset_password'),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), 
        name='password_reset_confirm'),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"), 
        name='password_reset_complete'),

    path('user/', views.userList, name='user'),
    path('userdetails/<str:pk>/', views.userDetails, name='userdetails'),
    path('updateuser/<str:pk>/', views.updateUser, name='updateuser'),
    


]