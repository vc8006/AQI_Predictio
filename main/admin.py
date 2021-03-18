from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Data , Test

admin.site.register(Test)

@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    list_display = ("Date","PM10","NO2","SO2","O3","AQI")
    pass