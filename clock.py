# from celery import shared_task
# from main.models import Data,Test
# from main.Ml_model import Ml_model as ml

import subprocess

# from celery.decorators import periodic_task
# from celery.task.schedules import crontab
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

data = Data()
@sched.scheduled_job('interval',minutes = 1)
def my_scheduled_job():
    subprocess.call('python manage.py scheduler'), shell=True, close_fds=True)
    # print("My job is running")
    # # print("My job is running")
    # Test.objects.create(name = "test")
    # ml.fun(ml.df)

# @periodic_task(run_every = (crontab(minute='*/1')))
# def run_objs():
#     my_scheduled_job.delay()

sched.start()