from django.urls import path

from core.views import CreateAppointmentView

app_name = 'core'

urlpatterns = [
    path('new_appointment/', CreateAppointmentView.as_view(), name='new-appointment'),
]