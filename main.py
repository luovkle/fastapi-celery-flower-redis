from fastapi import FastAPI

from celery_worker import send_email
from model import User

app = FastAPI()


@app.post("/users")
def create_user(user: User):
    send_email.delay(user.email)
    return {
        "msg": "A message has been sent to your email",
    }
