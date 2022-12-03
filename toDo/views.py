from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import ToDos
from django.contrib import messages


# Create your views here.
def index(request):
    tasks = ToDos.objects.all()
    context = {'tasks': tasks}
    return render(request, 'toDo/index.html', context)


def add(request):
    form = TaskForm
    context = {'form': form}
    if request.method == 'POST':
        task = request.POST.get('task')
        ToDos.objects.create(task=task)
        return redirect('index')
    return render(request, 'toDo/add.html', context)


def update(request, task_id):
    # get the task based on the specified id
    task = ToDos.objects.get(id=task_id)

    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        # update the database
        form.save()
        # redirect to index with update applied
        return redirect('index')
    return render(request, 'toDo/update.html', {'form': form})


def delete_task(request, task_id):
    # get the task based on the id
    task = ToDos.objects.get(id=task_id)
    # delete the task from the database
    task.delete()
    # redirect to index with delete applied
    return redirect('index')


def search(request):
    # get the search term entered by the user
    search_term = request.GET.get('search') or ''
    # search the database for search_term
    task = ToDos.objects.filter(task__icontains=search_term)
    context = {'tasks': task}
    return render(request, 'toDo/index.html', context)

