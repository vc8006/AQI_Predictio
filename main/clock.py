# from celery import shared_task
from .models import Data,Test
from . import Ml_model as ml

# from celery.decorators import periodic_task
# from celery.task.schedules import crontab
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

data = Data()
@sched.scheduled_job('interval',minutes = 1)
def my_scheduled_job():
    print("My job is running")
    Test.objects.create(name = "test")
    ml.fun(ml.df)

# @periodic_task(run_every = (crontab(minute='*/1')))
# def run_objs():
#     my_scheduled_job.delay()

sched.start()