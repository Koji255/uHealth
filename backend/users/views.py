from django.shortcuts import render, HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy

from users.forms import UserRegistrationForm, UserLoginForm, UserProfileForm


# Views here
def registration(request):
    """Registration view"""
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:user_login"))
        
    else:
        form = UserRegistrationForm()

    return render(request, "users/registration.html", {"form": form})


def login(request):
    """Login view"""
    if request.method == "POST":
        post = request.POST
        # Audit
        form = UserLoginForm(data=post)

        if form.is_valid():
            # Authentication
            if user := auth.authenticate(username=post["username"], 
                                         password=post["password"]):
                # Authorisation
                auth.login(request, user)

                return HttpResponseRedirect(reverse("index"))
    
    else:
        form = UserLoginForm()

    return render(request, "users/login.html", context={"form": form})


def profile(request):
    """Profile view"""
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UserProfileForm(instance=request.user, data=request.POST)

            if form.is_valid():
                form.save()

                return HttpResponseRedirect(reverse("users:user_profile"))
            
            else:
                print(form.errors)

        else:
            form = UserProfileForm(instance=request.user)

        return render(request, "users/profile.html", {"form": form})
    
    return HttpResponseRedirect(reverse("users:user_login"))


def logout(request):
    """Logout view"""
    auth.logout(request)

    return HttpResponseRedirect(reverse("core:index"))

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """Password change View"""
    template_name = "users/change_password.html"
    success_url = reverse_lazy("users:user_profile")