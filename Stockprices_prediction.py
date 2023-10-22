url = "https://www.youtube.com/watch?v=PuZY9q-aKLw"

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as webpip
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

#load data 

company = 'FB'

start = dt.datetime(2012, 1, 1)
end = dt.datetime(2020, 1, 1)

data = web.DataReader(company, 'yahoo', start, end)

#prepara date 
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

prediction_days = 60

x_train = []
y_train = []

for x in range(prediction_days, len(scaled_data)):
    x_train.append(scaled_data[x - prediction_days:x, 0 ])
    y_train.append(scaled_data(x, 0))

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train[1], 1))

# build model 
model = Sequential()

model.add(LSTM(unit=50, return_sequences=True, input_shape = (x_train.shape[1],1 )))
model.add(Dropout(0,2))
model.add(LSTM(unit=50, return_sequences=True))
model.add(Dropout(0,2))
model.add(LSTM(unit=50))
model.add(Dropout(0,2))
model.add(Dense(units = 1)) #this is the prediction of the next day 

model.compile(optimizer = 'adam', loss = 'mean_sqaured_error')
model.fit(x_train, y_train, epochs = 25, batch_size = 32)

'''' Test model on existing'''

#load test data 

test_start = dt.datetime(2020,1 ,1 )
test_end = dt.datetime.now()

test_data = web.DataReader(company, 'yahoo', test_start, test_end)
actual_price = test_data['Close'].values

total_dataset = pd.concat((data['Close'], test_data['Close']))

#check this line out 
model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].ValueError

model_inputs = model_inputs.reshape(-1,1 )
model_inputs .transform(model_inputs)

x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x - prediction_days: x , 0 ])