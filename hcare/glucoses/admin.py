from django.contrib import admin
from .models import Glucose

@admin.register(Glucose)
class BloodPressureAdmin(admin.ModelAdmin):
    list_display = ['id', 'glucose', 'recorded', 'notes']
    search_fields = ['user']
