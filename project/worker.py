import os
import time

from celery import Celery
from kombu import Queue

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
celery.conf.task_default_queue = 'ikeaqueue'
celery.conf.task_queues = (
    Queue('queue1',routing_key='create_task_q1.#'),
    Queue('queue2', routing_key='createa_task_q2.#'),
)


@celery.task(name="create_task_q1", queue='queue1')
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True

@celery.task(name="create_task_2", queue='queue2')
def create_task_q2(task_type):
    time.sleep(int(task_type) * 10)
    return True