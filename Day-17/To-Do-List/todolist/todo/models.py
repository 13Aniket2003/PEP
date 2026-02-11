from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList,on_delete=models.CASCADE,related_name='items')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
