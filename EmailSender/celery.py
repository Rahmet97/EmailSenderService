from __future__ import absolute_import

import os
import django

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmailSender.settings')
django.setup()

app = Celery('EmailSender')

app.conf.enable_utc = False
app.conf.update(timezone='Asia/Tashkent')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'Send_mail_to_Client': {
        'task': 'main.tasks.send_email',
        'schedule': 30
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
