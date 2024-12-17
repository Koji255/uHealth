from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.registration, name="user_registration"),
    path("login/", views.login, name="user_login"),
    path("profile/", views.profile, name="user_profile"),
    path("logout/", views.logout, name="user_logout"),
    path("password_change/", views.CustomPasswordChangeView.as_view(), 
         name="user_change_password"),
]