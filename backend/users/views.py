from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404

# Email confirmation
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from .forms import UserRegistrationForm
from .tokens import account_activation_token

from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from users.forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from users.models import User

from core.models import Appointment


# Views here
def signup(request):
    """Registration view"""
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserRegistrationForm(data=request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                subject = 'Подтвердите свою почту'

                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                    'html_message': 'message',
                })

                user.email_user(
                    subject, 
                    message,
                    html_message=message,
                )

                return HttpResponseRedirect(reverse('users:account_activation_sent'))
            
        else:
            form = UserRegistrationForm()

        return render(request, "users/signup.html", {"form": form})
    
    else:
        return HttpResponseRedirect(reverse('index'))


def account_activation_sent(request):
    return render(request, 'users/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect(reverse('users:account_activation_complete'))
    
    else:
        return HttpResponseBadRequest('Ссылка для активации недействительна')


def account_activation_complete(request):
    return render(request, 'users/account_activation_complete.html')    


def signin(request):
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

    return render(request, "users/signin.html", context={"form": form})



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
        
        appointments = Appointment.objects.filter(user_id=request.user.pk).all().order_by('-date_created')

        return render(request, "users/profile.html", context={
            "form": form,
            "appointments": appointments,
            })
    
    return HttpResponseRedirect(reverse("users:signin"))



def logout(request):
    """Logout view"""
    auth.logout(request)

    return HttpResponseRedirect(reverse("index"))



class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """Password change View"""
    template_name = "users/change_password.html"
    success_url = reverse_lazy("users:change_password_done")