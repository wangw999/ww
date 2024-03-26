from django.contrib import admin
from .models import Visits

# Register your models here.

@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
    pass