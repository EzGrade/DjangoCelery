from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .tasks import add
from celery.result import AsyncResult


class AddTaskView(ViewSet):
    def run_task(self, request, number1, number2):
        result = add.delay(number1, number2)
        return Response({"task_id": result.id})

    def get_task_result(self, request, task_id):
        task_result = AsyncResult(task_id)
        if task_result.ready():
            return Response({"status": task_result.state, "result": task_result.get()})
        else:
            return Response({"status": "pending"})
