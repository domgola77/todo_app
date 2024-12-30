from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed


@login_required
def task_list(request):
    if not request.user.is_superuser:
        return redirect('login')

    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)

    return render(request, 'task_list.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'user_type': 'admin'
    })


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


@login_required
def task_complete(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = True
        task.save()
        return redirect('task_list')
    return redirect('task_list')


@login_required
def task_delete(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')
    return redirect('task_list')
