from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Todo

# Create your views here.


def index(request):
    todo_list = Todo.objects.order_by('-deadline')
    context = {
        'todo_list': todo_list
    }
    return render(request, 'TUTodo/index.html', context)


def add(request):
    return render(request, 'TUTodo/add.html', None)


def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'TUTodo/edit.html', {'todo': todo})


def impressum(request):
    return render(request, 'TUTodo/impressum.html', None)


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'TUTodo/delete.html', {'todo': todo})
