import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date,timedelta
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.models import load_model
model = Sequential()
model=load_model('model.h5')
features = np.array([[30.0000000, 31.000000, 30.000000, 34919600]])
f=model.predict(features)
print(f)


