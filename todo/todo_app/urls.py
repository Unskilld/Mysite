from django.urls import path

from todo_app.views import ToDoView

urlpatterns = [
    path('home/', ToDoView.as_view(), name='todo')
]
