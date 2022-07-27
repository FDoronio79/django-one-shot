from django import forms
from todos.models import (
    ToDoList,
    ToDoItem,
)

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'

class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = '__all__'