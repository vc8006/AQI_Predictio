from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . import Ml_model as ml
from . import Scraper as sc
from datetime import date
import datetime
import pandas as pd
from .models import Update
from django.http import JsonResponse
from django.db.models import F

up_date = Update()

u = Update.objects.all().values()

def index(request):
    ans = ''
    ans2 = ''
    ans3 = ''
    ans4 = ''
    ans5 = ''
    d = ""
    x_new = ""
    if(request.method == 'POST'):
        x = request.POST.get('date')
        print(type(x))
        today = date.today()
        x_new = pd.to_datetime(x)
        if(x_new < today):
            print("****************************** less than ")
            # x = x.strftime("%m/%d/%Y")
            p = '"' + x + '"'
            y = ml.df.loc[x,'AQI']
            y2 = ml.df.loc[x,'SO2']
            y3 = ml.df.loc[x,'NO2']
            y4 = ml.df.loc[x,'O3']
            y5 = ml.df.loc[x,'PM10']
            # ans = "{:.2f}".format(y)
            # ans2 = "{:.2f}".format(y2)
            # ans3 = "{:.2f}".format(y3)
            # ans4 = "{:.2f}".format(y4)
            # ans5 = "{:.2f}".format(y5)
            ans = y
            ans2 = y2
            ans3 = y3
            ans4 = y4
            ans5 = y5
            

            d = x
        else:
            p = '"' + x + '"'
            y = ml.df_pred.loc[x,'AQI']
            y2 = ml.df_pred.loc[x,'SO2']
            y3 = ml.df_pred.loc[x,'NO2']
            y4 = ml.df_pred.loc[x,'O3']
            y5 = ml.df_pred.loc[x,'PM10']
            # ans = "{:.2f}".format(y)
            # ans2 = "{:.2f}".format(y2)
            # ans3 = "{:.2f}".format(y3)
            # ans4 = "{:.2f}".format(y4)
            # ans5 = "{:.2f}".format(y5)
            ans = y
            ans2 = y2
            ans3 = y3
            ans4 = y4
            ans5 = y5
            

            d = x

    max_date = "2021-03-19"

    today = date.today()


    last_data_date = ml.df_pred.index[-1]
    date_today = today
    last_data_date = pd.to_datetime(last_data_date)
    date_today = pd.to_datetime(date_today)
    date_difference = (last_data_date - date_today).days
    print(last_data_date)
    print(date_today)
    print(date_difference)
    la = last_data_date.date()
    # max_date ='"' + last_data_date.strftime("%y-%d-%m") + '"'
    max_date ='"' + la.strftime("%Y-%m-%d") + '"'
    # ml.fun()
    print(max_date)
    print(ans)

    # sc.scrap()
    # ml.fun(ml.df)
    print('555555555555555555 date1',ml.date1)
    print('555555555555555555 date2',ml.date2)

    # ml.u[0]['dat_up'] = ml.u[0]['dat_up'] + 1

    # update.dat_up.save()
 
    # print(ml.u[0]['dat_up'])

    # print(update)

    # u[0]['dat_up'] = 2
    # update.dat_up = 225
    # update.save()

    # up_date.dat_up = Update.objects.update(dat_up = F('dat_up') + 1)
    # up_date.save()

    # if(date_difference<4):
    #     ml.fun(ml.df,last_data_date)
    #     last_data_date += datetime.timedelta(days=1)
    #     max_date ='"' + last_data_date.strftime("%m/%d/%Y") + '"'
    #     print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhh',max_date)
        
    context = {'max' : max_date,'ans':ans,'ans2':ans2,'ans3':ans3,'ans4':ans4 ,'d':d , 'd1':ml.d1 , 'd2':ml.d2,'d3':ml.d3,'d4':ml.d4,'d5':ml.d5,'ans5':ans5}
    return render(request,'home.html',context)

