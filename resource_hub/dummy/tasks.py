# Demo Tasks
from resource_hub.celery import celery_app


@celery_app.task(name='task_test_celery', bind=True)
def task_test_celery(self):
    print(self.request)
    print(self.request.id)
    print("Hello World")
    task_test_celery.delay()
