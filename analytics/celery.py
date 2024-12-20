import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analytics.settings")

app = Celery("analytics")

app.config_from_object("django.conf:settings")

app.conf.timezone = "UTC"

app.autodiscover_tasks()
