from django.contrib import admin
from django import forms
from .models import TaskModel
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'completed', 'created_at')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'assigned_to':
            kwargs["queryset"] = User.objects.filter(is_superuser=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(TaskModel, TaskAdmin)
