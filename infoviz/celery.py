import os

from celery import Celery
from django.conf import settings  # noqa


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infoviz.settings')

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')

app = Celery('infoviz', broker='redis://127.0.0.1:6379')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.broker_url = BASE_REDIS_URL

app.conf.beat_schedule = {
    'Adding BTC to DB': {
        'task': 'api.tasks.add_bitcoin_to_db',
        'schedule': 60.0,
    },
    'Adding ETH to DB': {
        'task': 'api.tasks.add_ethereum_to_db',
        'schedule': 60.0,
    },
    'Adding SOL to DB': {
        'task': 'api.tasks.add_solana_to_db',
        'schedule': 60.0,
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')