from celery import shared_task 


@shared_task 
def test_task():
    return "This is a test task from Celery!"
