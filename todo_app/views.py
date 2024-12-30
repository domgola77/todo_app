from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


@login_required
def task_list(request):
    """
    Wyświetla listę zadań z komunikatem o zalogowanym użytkowniku.
    """
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    user_type = "admin" if request.user.is_superuser else "user"
    return render(request, 'task_list.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'user_type': user_type
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


def task_complete(request, pk):
    """
    Oznacza zadanie jako ukończone.
    """
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('task_list')


def task_delete(request, pk):
    """
    Usuwa zadanie.
    """
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
