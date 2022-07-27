from django import forms
from todos.models import (
    ToDoList,
    
)

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'