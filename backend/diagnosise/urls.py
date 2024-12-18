from django.urls import path

from diagnosise.views import *

app_name = "diagnosise"

urlpatterns = [
    path('ai-health-consultation/', ai_consultation, name='ai_consultation'),
    path('ai-answer/', TemplateView.as_view(template_name='results.html'),
         name='results'),
]