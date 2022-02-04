import os

from celery import Celery
from django.conf import settings  # noqa


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infoviz.settings')

#BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://redis:6379/0')

app = Celery('infoviz')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

#app.conf.broker_url = BASE_REDIS_URL

# Every 900 seconds = 15 minutes
app.conf.beat_schedule = {
    'Adding BTC to DB': {
        'task': 'api.tasks.add_bitcoin_to_db',
        'schedule': 900.0,
    },
    'Adding ETH to DB': {
        'task': 'api.tasks.add_ethereum_to_db',
        'schedule': 900.0,
    },
    'Adding SOL to DB': {
        'task': 'api.tasks.add_solana_to_db',
        'schedule': 900.0,
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')