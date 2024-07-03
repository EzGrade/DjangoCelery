from django.urls import path
from .views import AddTaskView

urlpatterns = [
    path('add/<int:number1>/<int:number2>', AddTaskView.as_view({"get": "run_task"}), name='run_task'),
    path('add/result/<str:task_id>/', AddTaskView.as_view({"get": "get_task_result"}), name='task_result'),
]
