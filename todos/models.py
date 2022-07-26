from tkinter import CASCADE
from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    task = models.CharField(max_length=100, null=True)
    due_date = models.DateTimeField(null=True)
    is_completed = models.BooleanField(default=False)
    list = models.ForeignKey(ToDoList, related_name="items", on_delete=models.CASCADE)

    def __str__(self):
        return self.task