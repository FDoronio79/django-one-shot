from django.urls import path

from todos.views import (
    ToDoListView
)

urlpatterns = [
    path("", ToDoListView.as_view(), name="todo_list_list"),
]