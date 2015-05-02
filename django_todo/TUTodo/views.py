from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from .models import Todo
from django.views import generic
import datetime

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'TUTodo/index.html'
    # auto generated todo_list var in index.html (context_object_name = 'todo_list' sparen wir uns)

    def get_queryset(self):
        return Todo.objects.order_by('-deadline')


def add(request):
    if request.POST:
        todo = Todo()
        try:
            todo.title = request.POST['title']
            todo.deadline = datetime.datetime.strptime(request.POST['deadline'], '%d.%m.%Y %H:%M')
            todo.finished = request.POST['finished']
        except KeyError:
            return HttpResponse('Es wurden nicht alle Daten angegeben!')
        except ValueError:
            pass
        try:
            todo.save()
        except ValidationError:
            return HttpResponse('Es wurden ungültige Daten angegeben!')
        return HttpResponseRedirect(reverse('TUTodo:index'))
    return render(request, 'TUTodo/add.html', None)


def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.POST:
        try:
            todo.title = request.POST['title']
        except KeyError:
            pass
        try:
            todo.deadline = datetime.datetime.strptime(request.POST['deadline'], '%d.%m.%Y %H:%M')
        except KeyError:
            pass
        except ValueError:
            pass
        try:
            todo.finished = request.POST['finished']
        except KeyError:
            pass
        try:
            todo.save()
        except ValidationError:
            return HttpResponse('Es wurden ungültige Daten angegeben!')
        return HttpResponseRedirect(reverse('TUTodo:index'))
    return render(request, 'TUTodo/edit.html', {'todo': todo})


def impressum(request):
    return render(request, 'TUTodo/impressum.html', None)


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.POST:
        if request.POST['delete'] == 'yes':
            todo.delete()
            if request.POST['json'] == True:
                return HttpResponse('{ok:true}');
            return HttpResponseRedirect(reverse('TUTodo:index'))
    return render(request, 'TUTodo/delete.html', {'todo': todo})
