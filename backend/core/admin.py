from django.contrib import admin
from core.models import Appointment

# Register your models here.
@admin.register(Appointment)
class DiagnosisAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    list_display = ('user', 'doctor', 'time', 'status', 'date_created')
    list_filter = ('status', 'doctor', 'time')