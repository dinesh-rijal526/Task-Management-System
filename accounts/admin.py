from django.contrib import admin
from .models import EmployeeModel

@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'employee_code')
