from django.contrib import admin
from .models import BloodPressure

@admin.register(BloodPressure)
class BloodPressureAdmin(admin.ModelAdmin):
    list_display = ['id', 'systolic', 'diastolic', 'pulse', 'recorded', 'notes']
    search_fields = ['user']

