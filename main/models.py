from django.db import models

# Create your models here.
class Data(models.Model):
    Date = models.DateField()
    PM10 = models.IntegerField()
    NO2 = models.IntegerField()
    SO2 = models.IntegerField()
    O3 = models.IntegerField()
    AQI = models.IntegerField()

    class Meta:
        db_table = "AQI_da"

class Test(models.Model):
    name = models.CharField(max_length = 100)