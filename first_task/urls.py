from django.urls import path
from .views import AddTaskView

urlpatterns = [
    path('add/', AddTaskView.as_view({"post": "run_task"}), name='run_task'),
    path('add/result/<str:task_id>/', AddTaskView.as_view({"get": "get_task_result"}), name='task_result'),
]
