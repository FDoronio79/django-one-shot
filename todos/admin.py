from django.contrib import admin
from todos.models import ToDoList, ToDoItem

admin.site.register(ToDoList)

admin.site.register(ToDoItem)