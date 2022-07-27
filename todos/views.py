from django.shortcuts import render
from django.views.generic.list import ListView
from todos.models import ToDoList

class ToDoListView(ListView):
    model = ToDoList
    template_name = "to_dos/list.html"
