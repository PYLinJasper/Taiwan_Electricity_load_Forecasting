from keras.models import Sequential
from keras.layers import Dense

import numpy as np
import matplotlib.pyplot as plt
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def transform_dataset(dataset, look_back=1):
    dataX = [dataset[i:(i + look_back)] for i in range(len(dataset) - look_back - 1)]
    dataY = [dataset[i + look_back] for i in range(len(dataset) - look_back - 1)]
    return np.array(dataX), np.array(dataY)


# Generate dummy data
look_back = 5

data = np.genfromtxt('../dataset/stock_2330.csv', delimiter=',', dtype=None)
prices = np.array([price for date, price in data]).astype(np.float64)

train_size = int(len(prices) * 0.8)
train, test = prices[:train_size], prices[train_size:]

trainX, trainY = transform_dataset(train, look_back)
testX, testY = transform_dataset(test, look_back)

# build model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=look_back))
model.add(Dense(units=1))
model.compile(loss='mse', optimizer='adam')

train_history = model.fit(trainX, trainY,
                          epochs=200, batch_size=5, shuffle=False,
                          validation_data=(testX, testY),
                          verbose=2)

# test = model.evaluate(testX, testY, batch_size=5, verbose=2)

model.save('stock_DNN_model.h5')


# Visualize
loss = train_history.history['loss']
val_loss = train_history.history['val_loss']


plt.subplot(121)
plt.plot(loss)
plt.subplot(122)
plt.plot(val_loss)
plt.show()
