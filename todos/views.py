from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'to_dos/detail.html', context)

def create_todo(request):
    form = ToDoListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("todo_list_list")
    context = {
        'form': form
    }
    return render(request, "to_dos/create.html", context)

def update_todo_list(request, pk):
    context = {}
    todo_list = get_object_or_404(ToDoList, pk=pk)
    form = ToDoListForm(request.POST or None, instance = todo_list)
    if form.is_valid():
        form.save()
        return redirect("todo_list_list")
    context["form"] = form

    return render(request, "to_dos/update.html", context)