from datetime import datetime
from .models import Url
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from datetime import timedelta
from django.db.models.functions import Now

@db_periodic_task(crontab(hour='*/1'))
def every_clean_up():
    to_delete = Url.objects.filter(created_at__lte=Now()-timedelta(hours=24))
    for url in to_delete:
        url.delete()





