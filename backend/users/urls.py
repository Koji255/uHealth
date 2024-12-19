from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.signup, name="signup"),
    path("login/", views.signin, name="signin"),
    path("profile/", views.profile, name="user_profile"),
    path("logout/", views.logout, name="user_logout"),
    path("password_change/", views.CustomPasswordChangeView.as_view(), 
         name="user_change_password"),
    path("password_changed/", PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'), name='change_password_done'),
    
    path("account_activation_sent/", views.account_activation_sent, name="account_activation_sent"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('account_activation_complete/', views.account_activation_complete, name='account_activation_complete'),
]