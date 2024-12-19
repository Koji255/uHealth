from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.forms import AppointmentForm

# Create your views here.
class CreateAppointmentView(LoginRequiredMixin, CreateView):
    form_class = AppointmentForm
    template_name = 'core/new_appointment.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('users:signin')

    def get_initial(self):
        # Initial values in form
        initial = super().get_initial()
        user = self.request.user

        initial.update({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': getattr(user, 'phone', ''),
        })

        return initial
    
    def form_valid(self, form):
        # Connection with current session user
        form.instance.user = self.request.user
        
        return super().form_valid(form)