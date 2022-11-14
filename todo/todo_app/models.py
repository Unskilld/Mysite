from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=80)
    context = models.CharField(max_length=80, blank=True)
    is_done = models.BooleanField(default=False)
    is_today = models.BooleanField(default=False)

    def __str__(self):
        return self.title
