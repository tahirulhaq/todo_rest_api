# from django.conf.urls import url
from django.urls import path, include
from .views import (
    TodoListApiView,
    TodomyView,
)

urlpatterns = [
    path('', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodomyView.as_view()),
]
