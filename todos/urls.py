from django.urls import path

from todos.views import (
    show_todos,
    todos_details,
    create_todo,
)

urlpatterns = [
    path("", show_todos, name="todo_list_list"),
    path("<int:pk>/", todos_details, name="todo_list_detail"),
    path("create-todo/", create_todo, name="todo_list_create"),
]