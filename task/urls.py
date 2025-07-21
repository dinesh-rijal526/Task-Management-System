from django.urls import path, include
from .views import *

urlpatterns = [
    path('', task_list , name='task_list'),
    path('create-task/', create_task, name='create_task'),
    path('tasks/<int:task_id>/complete/', mark_task_completed, name='mark_completed'),
    path('logout/', logout_view, name='logout'),
]