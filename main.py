from fastapi import FastAPI

from celery_worker import send_email, celery
from model import User

app = FastAPI()


@app.post("/users")
def create_user(user: User):
    task = send_email.delay(user.email)
    return {
        "task_id": task.id,
    }


@app.get("/tasks")
def read_task(task_id: str):
    task_result = celery.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
