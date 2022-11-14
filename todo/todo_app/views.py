from django.views.generic import *

from todo_app.models import ToDoList


class ToDoView(ListView):
    model = ToDoList
    queryset = ToDoList.objects.all()
    template_name = 'todoapp/todo_template.html'
    context_object_name = 'ToDoList'
