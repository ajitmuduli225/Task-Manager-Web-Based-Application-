from django.shortcuts import render,redirect

# Create your views here.
from task.manager import *






task_manager = TaskManager()

def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        status = request.POST['status']
        task_manager.add_task(title, description, priority, status)
        return redirect('view_all_tasks')
    return render(request, 'add_task.html')

def edit_task(request, task_id):
    task = task_manager.get_task_by_id(task_id)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        status = request.POST['status']
        task_manager.edit_task(task_id, title, description, priority, status)
        return redirect('view_all_tasks')
    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, task_id):
    task_manager.delete_task(task_id)
    return redirect('view_all_tasks')

def view_all_tasks(request):
    tasks = task_manager.view_all_tasks()
    return render(request, 'view_all_tasks.html', {'tasks': tasks})

def filter_tasks_by_priority(request):
    priority = request.GET.get('priority')
    tasks = task_manager.filter_tasks_by_priority(priority)
    return render(request, 'view_all_tasks.html', {'tasks': tasks})