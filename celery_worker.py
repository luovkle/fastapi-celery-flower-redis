import time
import random

from celery import Celery
from celery.utils.log import get_task_logger

celery = Celery(
    "tasks",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="redis://redis:6379/0",
)

celery_log = get_task_logger(__name__)


@celery.task
def send_email(email: str):
    time.sleep(random.randint(1, 4))
    celery_log.info("Email has been sent")
    return {
        "msg": f"Email has been sent to {email}",
        "details": {
            "destination": email,
        },
    }
