from venv import create
from django.urls import path

from todos.views import (
    delete_todo_list,
    show_todos,
    todos_details,
    create_todo,
    update_todo_list,
    delete_todo_list,
    create_item,
)

urlpatterns = [
    path("", show_todos, name="todo_list_list"),
    path("<int:pk>/", todos_details, name="todo_list_detail"),
    path("create-todo/", create_todo, name="todo_list_create"),
    path("<int:pk>/edit/", update_todo_list, name="todo_list_update"),
    path("<int:pk>/delete", delete_todo_list, name="todo_list_delete"),
    path("items/create/", create_item, name="todo_item_create")
]