from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name