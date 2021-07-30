from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path, reverse_lazy
from django.urls.conf import include
from .views import HomeView, AboutView
from django.contrib.auth import views as auth_views
from . import views
from .forms import EmailValidationOnForgotPassword

urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    path('about/',AboutView.as_view() , name='about'),

    path('contact/',views.contact, name='contact'),
    path("blog/", views.blog , name='blogHome'),
    

    
    path('signup/', views.signup, name='signup'),
    
    path('login/',auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/',views.handleLogout , name='handleLogout'),
   
    

    #change password
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name="home/change-password.html",success_url=reverse_lazy('change_password_done')) , name='change_password'),
    #success_url is also a way to redirect a user after changing the password successfully.
    #reverse_lazy is used for resolving Django URL names into URL paths. 
    path('change_password_done/',auth_views.PasswordChangeDoneView.as_view(
         template_name="home/change-password_done.html") , name='change_password_done'),
    


    #reset-password
    # for reset password we have 4 different django in-built views and 2 forms password-reset-form and password-reset-confirm
    path('password-reset/',

         auth_views.PasswordResetView.as_view(
              form_class=EmailValidationOnForgotPassword,
             template_name='password-reset/password_reset_form.html',
             subject_template_name='password-reset/password_reset_subject.txt',
             email_template_name='password-reset/password_reset_email.html',
          
             ),
         name='password_reset'),
    
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password-reset/password_reset_done.html'),name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password-reset/password_reset_confirm.html'),name='password_reset_confirm'),
    #uid: The user’s primary key encoded in base 64
    #token: Token to check that the reset link is valid
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password-reset/password_reset_complete.html'),name='password_reset_complete'),

]




    # path('signup/',views.handleSignup , name='handleSignup'),
#      path('login/',auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
#     path('logout/',auth_views.LogoutView.as_view(template_name='home/home.html'), name='logout',),
# path('login/',views.handleLogin , name='handleLogin'),


# success_url = '/'