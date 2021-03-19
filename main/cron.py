from . import Ml_model as ml
from .models import Test , Data

data = Data()
def my_scheduled_job():
    Test.objects.create(name = "test")
    # data.AQI = 2
    # data.save()
    ml.fun(ml.df)
    # print("hhhhhhhhhhhhhhheeeeeeeeeeeeeellllllllll")  
    # python manage.py runserver