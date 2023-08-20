import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date,timedelta
from tensorflow import keras
today=date.today()
d1=today.strftime("%Y-%m-%d")
end_date=d1
d2=date.today()-timedelta(days=365)
d2=d2.strftime("%Y-%m-%d")
start_date=d2
df=yf.download('TATAMOTORS.NS',start=start_date,end=end_date,progress=False)
print(df)
df['Date']=df.index
data=df[["Date","Open","High","Low","Close","Adj Close","Volume"]]
a=data.reset_index(drop=True, inplace=True)
b=data.tail()
print(a,b)
import plotly.graph_objects as go
figure=go.Figure(data=[go.Candlestick(x=data['Date'],open=data['Open'],high=data['High'],low=data['Low'],close=data['Close'])])
figure.update_layout(title="TATA MOTORS STOCK PRICE ANALYSIS",xaxis_rangeslider_visible=False)
c=figure.show()
print(c)
correlation = data.corr()
print(correlation["Close"].sort_values(ascending=False))
x = data[["Open", "High", "Low", "Volume"]]
y = data["Close"]
x = x.to_numpy()
y = y.to_numpy()
y = y.reshape(-1, 1)

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
from keras.models import Sequential
from keras.layers import Dense, LSTM
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape= (xtrain.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
d=model.summary()
print(d)
model.compile(optimizer='adam', loss='mean_squared_error')
e=model.fit(xtrain, ytrain, batch_size=1, epochs=10)
print(e)
model.save('model.h5')

