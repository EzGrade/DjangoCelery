from celery import Celery

app = Celery('tasks')


@app.task(bind=True, ignore_result=False)
def add(self, x, y):
    return x + y
