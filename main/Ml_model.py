import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('/home/vedant/djano_self/mysite/main/templates/city_day.csv',index_col=[1],parse_dates=True,squeeze=True)
df.head()

df=df[df['City']=='Delhi']
df[df['AQI'].isnull()]
df.fillna(method='ffill', inplace = True)
df = df.drop(columns=['City','AQI_Bucket'])
df = df.asfreq('d')

df_ma = df.rolling(window=30).mean()

cols =  list(df.columns)
df_base = pd.concat([df,df.shift(1)],axis = 1)
col2 = ['f_PM2.5','f_PM10','f_NO','f_NO2','f_NOx','f_NH3','f_CO','f_SO2','f_O3','f_Benzene','f_Toluene','f_Xylene','f_AQI']
f_col = cols + col2
df_base.columns = f_col
df_base.dropna(inplace = True)

from sklearn.metrics import mean_squared_error
import statsmodels.graphics.tsaplots as sgt

from statsmodels.tsa.arima_model import ARIMA
size =  int(len(df)*0.8)
df_train = df.iloc[:size]
df_test = df.iloc[size:]

from pandas.tseries.offsets import DateOffset
future_dates = [df.index[-1] + DateOffset(days = x)for x in range(30)]

future_datest_df = pd.DataFrame(index = future_dates[1:],columns=df.columns)


model = ARIMA(df_train['AQI'],order = (2,1,2))
model_fit = model.fit()
future_datest_df['AQI'] = model_fit.forecast(steps = 29)[0]

model = ARIMA(df_train['SO2'],order = (2,1,2))
model_fit = model.fit()
future_datest_df['SO2'] = model_fit.forecast(steps = 29)[0]

model = ARIMA(df_train['NO2'],order = (2,1,2))
model_fit = model.fit()
future_datest_df['NO2'] = model_fit.forecast(steps = 29)[0]

model = ARIMA(df_train['CO'],order = (2,1,2))
model_fit = model.fit()
future_datest_df['CO'] = model_fit.forecast(steps = 29)[0]

df = pd.concat([df,future_datest_df])

d1 = df['AQI'][-60:].tolist()
d2 = df.index[-60:].strftime('%Y-%m-%d').tolist()

d3 = df['SO2'][-60:].tolist()
d4 = df['NO2'][-60:].tolist()
d5 = df['CO'][-60:].tolist()
