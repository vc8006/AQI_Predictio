import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from .models import Data
from datetime import date
import datetime

data = Data()
# print(new_dta)
q = Data.objects.all().values()
df = pd.DataFrame(q)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index(df['Date']) 

# df = pd.read_csv('./main/static/city_day.csv',index_col=[1],parse_dates=True,squeeze=True)
# df.head()

# df=df[df['City']=='Delhi']
# df[df['AQI'].isnull()]
# df.fillna(method='ffill', inplace = True)
# df = df.drop(columns=['City','AQI_Bucket'])
# df = df.asfreq('d')

# df_ma = df.rolling(window=30).mean()

# cols =  list(df.columns)
# df_base = pd.concat([df,df.shift(1)],axis = 1)
# col2 = ['f_PM2.5','f_PM10','f_NO','f_NO2','f_NOx','f_NH3','f_CO','f_SO2','f_O3','f_Benzene','f_Toluene','f_Xylene','f_AQI']
# f_col = cols + col2
# df_base.columns = f_col
# df_base.dropna(inplace = True)

from sklearn.metrics import mean_squared_error
import statsmodels.graphics.tsaplots as sgt

from statsmodels.tsa.arima_model import ARIMA
size =  int(len(df)*0.8)
df_train = df.iloc[:size]
df_test = df.iloc[size:]

# df_new = pd.read_csv('./main/static/newest.csv',index_col=[0],parse_dates=True,squeeze=True)
# df_new.fillna(method='ffill', inplace = True)
# df_new = df_new.asfreq('d')
# df = pd.concat([df,df_new])

# df.dropna(inplace = True,axis = 1)
from pandas.tseries.offsets import DateOffset
# future_dates = [df.index[-1] + DateOffset(days = x)for x in range(7)]

# future_datest_df = pd.DataFrame(index = future_dates[1:],columns=df.columns)
# model = ARIMA(df_train['AQI'],order = (2,1,2))
# model_fit = model.fit()
# future_datest_df['AQI'] = model_fit.forecast(steps = 6)[0]

# model = ARIMA(df_train['SO2'],order = (2,1,2))
# model_fit = model.fit()
# future_datest_df['SO2'] = model_fit.forecast(steps = 6)[0]

# model = ARIMA(df_train['NO2'],order = (2,1,2))
# model_fit = model.fit()
# future_datest_df['NO2'] = model_fit.forecast(steps = 6)[0]

# model = ARIMA(df_train['O3'],order = (2,1,2))
# model_fit = model.fit()
# future_datest_df['O3'] = model_fit.forecast(steps = 6)[0]

# model = ARIMA(df_train['PM10'],order = (2,1,2))
# model_fit = model.fit()
# future_datest_df['PM10'] = model_fit.forecast(steps = 6)[0]

# df = pd.concat([df,future_datest_df])

# max_date_last = date("2021-03-21")
# max_date_last = date(2021, 3, 21)

def fun(df):
    from pandas.tseries.offsets import DateOffset
    # data.DATE  = date(2021, 3, 21)
    # max_date_last += datetime.timedelta(days=1)
    future_dates = [df.index[-1] + DateOffset(days = x)for x in range(2)]
    future_datest_df_new = pd.DataFrame(index = future_dates[1:],columns=df.columns)
    # data.DATA = pd.to_datetime(df['Date'])
    # data.DATE = df['Date']
    # df1 = df.set_index(df['Date']) 

    model = ARIMA(df_train['AQI'],order = (2,1,2))
    model_fit = model.fit()
    data.AQI = model_fit.forecast(steps = 1)[0]
    # future_datest_df_new['AQI'] = model_fit.forecast(steps = 1)[0]

    model = ARIMA(df_train['SO2'],order = (2,1,2))
    model_fit = model.fit()
    data.SO2 = model_fit.forecast(steps = 1)[0]
    # future_datest_df_new['SO2'] = model_fit.forecast(steps = 1)[0]

    model = ARIMA(df_train['NO2'],order = (2,1,2))
    model_fit = model.fit()
    data.NO2 = model_fit.forecast(steps = 1)[0]
    # future_datest_df_new['NO2'] = model_fit.forecast(steps = 1)[0]

    model = ARIMA(df_train['O3'],order = (2,1,2))
    model_fit = model.fit()
    data.O3 = model_fit.forecast(steps = 1)[0]
    # future_datest_df_new['O3'] = model_fit.forecast(steps = 1)[0]

    model = ARIMA(df_train['PM10'],order = (2,1,2))
    model_fit = model.fit()
    data.PM10 = model_fit.forecast(steps = 1)[0]
    # future_datest_df_new['PM10'] = model_fit.forecast(steps = 1)[0]

    # df = pd.concat([df,future_datest_df_new])
    # print(df.tail())
    data.Date = future_dates[1].strftime('%Y-%m-%d')
    # data.AQI = model_fit.forecast(steps = 1)[0] 
    # data.SO2 = model_fit.forecast(steps = 1)[0]
    # data.NO2 = model_fit.forecast(steps = 1)[0]
    # data.O3 = model_fit.forecast(steps = 1)[0]
    # data.PM10 = model_fit.forecast(steps = 1)[0]
    print("hhhhhhhhhhhhh",type(data.Date))

    data.save()
    # print(future_dates[1].strftime('%Y-%m-%d'))
    # print(future_datest_df_new['AQI'])
    # return df
# df = fun(df)
# (df.tail)
d1 = df['AQI'][-30:].tolist()
d2 = df.index[-30:].strftime('%Y-%m-%d').tolist()

d3 = df['SO2'][-30:].tolist()
d4 = df['NO2'][-30:].tolist()
d5 = df['O3'][-30:].tolist()

print(df['Date'])
print(df.tail())
# fun(df)
# data.AQI = int(data.AQI)
# print(type(data.AQI))