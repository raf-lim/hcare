release: python manage.py migrate
{%- if cookiecutter.use_async == "y" %}
web: gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker
{%- else %}
web: gunicorn config.wsgi:application
{%- endif %}
{%- if cookiecutter.use_celery == "y" %}
worker: REMAP_SIGTERM=SIGQUIT celery -A config.celery_app worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery -A config.celery_app beat --loglevel=info
{%- endif %}

