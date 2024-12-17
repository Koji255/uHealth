from django.contrib import admin
from .models import Diagnosis

# Register your models here.

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    readonly_fields = ('symptoms', 'disease_category', 'description', 'date_created')
    list_display = ('user', 'disease_category', 'date_created')
