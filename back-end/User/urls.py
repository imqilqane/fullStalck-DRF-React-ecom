from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('register/verifing/',
         views.UserAccountVerification.as_view(), name='verifing'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('new-password-request/',
         views.RequestPasswordResetView.as_view(), name='new_password'),
    path('reset-password/<str:uidb64>/<str:token>/',
         views.ResetPasswordView.as_view(), name='reset'),
    path('logout/', views.LogOutView.as_view(), name='logout')

]
