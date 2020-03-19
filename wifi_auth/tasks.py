# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery.task import periodic_task
from celery.schedules import crontab
from .models import Router
import os
@periodic_task(run_every=crontab(minute='*/1*'),name='ping_routers')
def ping_routers():
    routers = Router.objects.all()
    for router in routers:
        response = os.system("ping -c 1 " + router.ip_address)
        if response == 0:
            router.available = True
            router.save()
            print("router is ok, saved")
        else:
            router.available = False
            router.save()
            print("router is down, saved")
