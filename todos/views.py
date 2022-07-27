from django.shortcuts import render, redirect, get_object_or_404
from todos.models import TodoItem, TodoList
from todos.forms import TodoListForm, TodoItemForm

def show_todos(request):
    todolists = TodoList.objects.all()
    context = {"todolists": todolists}
    return render(request, 'to_dos/list.html', context)

def todos_details(request, pk):
    todoitem = TodoList.objects.get(pk=pk)
    context = {
        "todoitem": todoitem
    }
    return render(request, 'to_dos/detail.html', context)

def create_todo(request):
    form = TodoListForm(request.POST or None)
    if form.is_valid():
        todo = form.save()
        return redirect("todo_list_detail", pk=todo.pk)
    context = {
        'form': form
    }
    return render(request, "to_dos/create.html", context)

def update_todo_list(request, pk):
    context = {}
    todo_list = get_object_or_404(TodoList, pk=pk)
    form = TodoListForm(request.POST or None, instance = todo_list)
    if form.is_valid():
        todo = form.save()
        return redirect("todo_list_detail", pk=todo.pk)
    context["form"] = form

    return render(request, "to_dos/update.html", context)

def delete_todo_list(request, pk):
    context = {}
    todo_list = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        todo_list.delete()
        return redirect("todo_list_list")

    return render(request, "to_dos/delete.html", context)

def create_item(request):
    form = TodoItemForm(request.POST or None)
    if form.is_valid():
        todo = form.save()
        return redirect("todo_list_detail", pk=todo.list.pk)
    context = {
        'form': form
    }
    return render(request, "to_dos/create_item.html", context)

def update_todo_item(request, pk):
    context = {}
    todo_item = get_object_or_404(TodoItem, pk=pk)
    form = TodoItemForm(request.POST or None, instance = todo_item)
    if form.is_valid():
        todo = form.save()
        return redirect("todo_list_detail", pk=todo.list.pk)
    context["form"] = form

    return render(request, "to_dos/update_item.html", context)