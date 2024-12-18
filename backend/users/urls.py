from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.registration, name="user_registration"),
    path("login/", views.login, name="user_login"),
    path("profile/", views.profile, name="user_profile"),
    path("logout/", views.logout, name="user_logout"),
    path("password_change/", views.CustomPasswordChangeView.as_view(), 
         name="user_change_password"),
    path("password_changed/", PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'), name='change_password_done'),
]