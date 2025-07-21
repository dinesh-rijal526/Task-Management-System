from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.decorators import user_passes_test
from .models import TaskModel
from .forms import TaskForm
# Create your views here.

User = get_user_model()

@login_required
def task_list(request):
    if request.user.is_superuser:
        tasks = TaskModel.objects.all()
    else:
        tasks = TaskModel.objects.filter(assigned_to=request.user)

    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'create_task.html', {'form': form})

@login_required
def mark_task_completed(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)

    if request.method == "POST" and request.user == task.assigned_to or request.user.is_superuser:
        task.completed = True
        task.save()

    return redirect('task_list')

def logout_view(request):
    logout(request)
    return redirect('/admin/login/')