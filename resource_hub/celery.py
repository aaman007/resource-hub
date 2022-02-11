from celery import Celery


class CeleryConfig:
    broker_url = 'redis://broker:6379/0'
    # result_backed = 'rpc://'

    task_serializer = 'json'
    # result_serializer = 'json'
    timezone = 'UTC'
    enable_utc = True

    imports = [
        'resource_hub.dummy.tasks'
    ]

    # For setting queue for tasks
    task_routes = {
        'resource_hub.dummy.tasks.*': {'queue': 'dummy-queue'}
    }

    # for rate-limiting tasks
    task_annotations = {
        # 'tasks.task_send_email': {'rate_limit': '10/m'}  # 10 task per minute
        'resource_hub.dummy.tasks.task_test_celery': {'rate_limit': '10/m'}
    }


def create_celery_app():
    app = Celery('resource_hub')
    app.config_from_object(CeleryConfig)
    return app


celery_app = create_celery_app()
