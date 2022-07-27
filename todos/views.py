from django.shortcuts import render, redirect
from todos.models import ToDoList
from todos.forms import ToDoListForm

def show_todos(request):
    todolists = ToDoList.objects.all()
    context = {"todolists": todolists}
    return render(request, 'to_dos/list.html', context)

def todos_details(request, pk):
    todoitem = ToDoList.objects.get(pk=pk)
    context = {
        "todoitem": todoitem
    }
    return render(request, 'to_dos/details.html', context)

def create_todo(request):
    form = ToDoListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("todo_list_list")
    context = {
        'form': form
    }
    return render(request, "to_dos/create.html", context)
