web: pipenv run gunicorn 'service.microservice:start_service()'
worker: celery --app=tasks.celery_app worker