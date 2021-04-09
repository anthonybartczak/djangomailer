from celery import Celery
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery()

@shared_task
def test():
    print("The sample task just ran.")