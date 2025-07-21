from django.contrib import admin
from django import forms
from django.contrib.auth import get_user_model
from .models import TaskModel

User = get_user_model()

class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(is_superuser=False) # type: ignore
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'assigned_to']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(is_superuser=False) # type: ignore



    

