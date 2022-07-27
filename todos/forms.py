from django import forms
from todos.models import (
    TodoList,
    TodoItem,
)

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'
