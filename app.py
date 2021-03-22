import argparse
#coding=utf-8
import pandas as pd
import numpy as np
from keras.models import Sequential,Model
from keras.layers import Dense, Dropout, Activation, Flatten, LSTM, TimeDistributed, RepeatVector,Input
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt
from keras.utils import to_categorical
from tensorflow.python.keras.callbacks import LearningRateScheduler
# %matplotlib inline

def normalize(df):
    norm = df.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
    return norm
def train_windows(df, ref_day, predict_day):
    X_train, Y_train = [], []
    for i in range(df.shape[0]-predict_day-ref_day):
        X_train.append(np.array(df.iloc[i:i+ref_day,:-1]))
        Y_train.append(np.array(df.iloc[i+ref_day:i+ref_day+predict_day]["y"]))
    return np.array(X_train), np.array(Y_train)
def lstm_stock_model(shape):
    model = Sequential()
    model.add(LSTM(64, input_shape=(shape[1], shape[2]), return_sequences=True, dropout=0.2))
    model.add(LSTM(64, return_sequences=True, dropout=0.2))

    # model.add(TimeDistributed(Dense(1)))
    model.add(Flatten())
    model.add(Dense(7,activation='linear'))
    model.add(Dense(7))
    model.compile(loss="mae", optimizer="Adam",metrics=['mae'])
    model.summary()
    return model
def scheduler(epoch):
    #change the learning rate at whether epoch you like
    if epoch > 100:
        lr = 1e-4/2
        return lr
    elif epoch > 30:
        lr = 1e-4
        return lr
    else:
        lr = 1e-3
        return lr
    return lr

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # training data import
    parser.add_argument('--training', default='training_data.csv',
    help='input training data file name')
    # predict data export
    parser.add_argument('--output', default='submission.csv',
    help='output file name')
    # print("No problem ")

    args = parser.parse_args()

    train = pd.read_csv(args.training)
    
    train['y'] = train['備轉容量'].shift(-7)
    train['臺北最低氣溫(℃)'] = train['臺北最低氣溫(℃)'].shift(-7)
    train['新北最低氣溫(℃)'] = train['新北最低氣溫(℃)'].shift(-7)
    train['高雄最低氣溫(℃)'] = train['高雄最低氣溫(℃)'].shift(-7)
    train['臺北最高氣溫(℃)'] = train['臺北最高氣溫(℃)'].shift(-7)
    train['新北最高氣溫(℃)'] = train['新北最高氣溫(℃)'].shift(-7)
    train['高雄最高氣溫(℃)'] = train['高雄最高氣溫(℃)'].shift(-7)
    train.iloc[:,1:8] = normalize(train.iloc[:,1:8])
    target = train[len(train.values)-14:len(train.values)-7]
    train = train.dropna()
    del target['y']

    test = train[-150:]
    #train & test
    train = train.reset_index()
    test = test.reset_index()
    target = target.reset_index()
    train = train.dropna()

    train.drop(['日期', 'index'], axis=1, inplace=True)
    test.drop(['日期', 'index'], axis=1, inplace=True)
    target.drop(['日期', 'index'], axis=1, inplace=True)

    X_train, Y_train = train_windows(train, 7, 7)
    X_test, Y_test = train_windows(test, 7, 7)

    tar_X = []
    for i in range(0,7):
        tar_X.append(target.values[i].tolist())
    Rtar_X = []
    Rtar_X.append(tar_X)
    tar_X = np.array(Rtar_X)
    tar_X[0]

    model = lstm_stock_model(X_train.shape)
    change_lr = LearningRateScheduler(scheduler)
    callback = [EarlyStopping(monitor="mae", patience=10, verbose=1, mode="auto"), change_lr]
    history = model.fit(X_train, Y_train, epochs=200, batch_size=16, validation_split=0.2, shuffle=False)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.legend(loc = 'upper right')

    result = pd.DataFrame(model.predict(tar_X)[0].tolist())
    result.insert(0, "date", [20210323,20210324,20210325,20210326,20210327,20210328,20210329], True) 
    result.columns =['Date', 'Predict Result'] 
    result.to_csv(args.output)
    
    # result.to_csv(args.output, index=0)