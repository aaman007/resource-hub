celery -A resource_hub.celery worker               
celery -A resource_hub.celery --broker=redis://localhost:63790 flower