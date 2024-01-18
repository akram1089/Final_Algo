# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superlogo.settings')

# create a Celery instance and configure it using the settings from Django
app = Celery('superlogo')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-two-number': {
        'task': 'home.tasks.add',
        'schedule': crontab(hour=16, minute=6),
        'args': (2, 3),  # Provide the arguments for your task here
    }
}
app.autodiscover_tasks(['home'])  # Add the app name where your tasks are defined

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))





