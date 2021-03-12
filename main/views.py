from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . import Ml_model as ml

def index(request):
    ans = ''
    ans2 = ''
    ans3 = ''
    ans4 = ''
    d = ""
    if(request.method == 'POST'):
        x = request.POST.get('date')
        p = '"' + x + '"'
        y = ml.future_datest_df.loc[x,'AQI']
        y2 = ml.future_datest_df.loc[x,'SO2']
        y3 = ml.future_datest_df.loc[x,'NO2']
        y4 = ml.future_datest_df.loc[x,'CO']
        ans = y
        ans2 = y2
        ans3 = y3
        ans4 = y4
        d = p
    context = {'ans':ans,'ans2':ans2,'ans3':ans3,'ans4':ans4 ,'d':d , 'd1':ml.d1 , 'd2':ml.d2,'d3':ml.d3,'d4':ml.d4,'d5':ml.d5}
    return render(request,'home.html',context)