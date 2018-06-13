# DAVIDRVU 2018

# SOURCE: https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/

from datetime import datetime
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import Sequential
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import math
import numpy as np
import os
import pandas as pd
import sys

sys.path.insert(0, "../../data_science_utils")
from get_dir_file_ext import get_dir_file_ext

def parse(x):
    return datetime.strptime(x, '%Y %m %d %H')

def load_data(original_data_set_file):
    [directory, filename_base, file_extension] = get_dir_file_ext(original_data_set_file)

    dataset = pd.read_csv(original_data_set_file,  parse_dates = [['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
    dataset.drop('No', axis=1, inplace=True)
    # manually specify column names
    dataset.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
    dataset.index.name = 'date'
    # mark all NA values with 0
    dataset['pollution'].fillna(0, inplace=True)
    # drop the first 24 hours
    dataset = dataset[24:]
    # summarize first 5 rows
    print(dataset.head(5))
    # save to file
    filename_output = directory + "\\pollution.csv"
    dataset.to_csv(filename_output)
    return filename_output

def show_data(data_in):
    # load dataset
    dataset = pd.read_csv(data_in, header=0, index_col=0)
    values = dataset.values
    # specify columns to plot
    groups = [0, 1, 2, 3, 5, 6, 7]
    i = 1
    # plot each column
    pyplot.figure()
    for group in groups:
        pyplot.subplot(len(groups), 1, i)
        pyplot.plot(values[:, group])
        pyplot.title(dataset.columns[group], y=0.5, loc='right')
        i += 1
    pyplot.show()

# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg

def lstm_core(data_in):
    # load dataset
    dataset = pd.read_csv(data_in, header=0, index_col=0)

    print("dataset = ")
    print(dataset)
    print(dataset.shape)
    os.system("pause")

    values = dataset.values
    print("values = ")
    print(values)
    print(values.shape)
    os.system("pause")

    # integer encode direction
    encoder = LabelEncoder()
    values[:,4] = encoder.fit_transform(values[:,4])

    print("values = ")
    print(values)
    print(values.shape)
    os.system("pause")

    # ensure all data is float
    values = values.astype('float32')
    #values = np.float32(values)
    # normalize features
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)

    print("scaled = ")
    print(scaled)
    print(scaled.shape)
    os.system("pause")

    # specify the number of lag hours
    n_hours    = 3
    n_features = 8
    # frame as supervised learning
    reframed = series_to_supervised(scaled, n_hours, 1) # TODOTODO: PROBAR series_to_supervised(scaled, 1, 1)

    print("reframed = ")
    print(reframed)
    print(reframed.shape)
    os.system("pause")
     
    # split into train and test sets
    print("split into train and test sets ...")
    values = reframed.values

    print("values (2) = ")
    print(values)
    print(values.shape)
    os.system("pause")

    n_train_hours = 365 * 24
    train = values[:n_train_hours, :]
    test  = values[n_train_hours:, :]

    num_filas = values.shape[0]

    # pyplot train and test
    pyplot.plot(list(range(0, n_train_hours)), train[:, -n_features], 'bo-', label='Train')
    pyplot.plot(list(range(n_train_hours, num_filas)), test[:,  -n_features], 'ko-', label='Test')
    pyplot.legend()
    pyplot.show()

    # split into input and outputs
    n_obs = n_hours * n_features  # 24 = (3 * 8)

    train_X, train_y = train[:, :n_obs], train[:, -n_features]
    test_X, test_y   = test[:, :n_obs], test[:, -n_features]

    print("train_X.shape = ")
    print(train_X.shape )
    print("train_y.shape = ")
    print(train_y.shape )
    print("test_X.shape = ")
    print(test_X.shape )
    print("test_y.shape = ")
    print(test_y.shape )

    os.system("pause")

    # reshape input to be 3D [samples, timesteps, features]
    print("\nReshape input to be 3D [samples, timesteps, features]")
    train_X = train_X.reshape((train_X.shape[0], n_hours, n_features))
    test_X  = test_X.reshape((test_X.shape[0], n_hours, n_features))

    print("train_X.shape = ")
    print(train_X.shape )
    print("train_y.shape = ")
    print(train_y.shape )
    print("test_X.shape = ")
    print(test_X.shape )
    print("test_y.shape = ")
    print(test_y.shape )

    os.system("pause")
     
    # design network
    print("\nDesign network ...")
    model = Sequential()
    model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')

    # fit network
    print("\nFit network ...")
    #history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)
    history = model.fit(train_X, train_y, epochs=50, batch_size=72, verbose=2, shuffle=False)
    
    # plot history
    print("\nPlot history ...")
    pyplot.plot(history.history['loss'], label='train')
    #pyplot.plot(history.history['val_loss'], label='test')
    pyplot.legend()
    pyplot.show()
     
    # make a prediction
    print("\nMake a prediction ...")
    yhat = model.predict(test_X)

    print("yhat.shape = ")
    print(yhat.shape)

    os.system("pause")

    pyplot.plot(list(range(0, n_train_hours)), train[:, -n_features], 'bo-', label='Train')
    pyplot.plot(list(range(n_train_hours, num_filas)), test[:,  -n_features], 'ko-', label='Test True')
    pyplot.plot(list(range(n_train_hours, num_filas)), yhat, 'go-', label='Test Predicted')
    pyplot.legend()
    pyplot.show()

    test_X = test_X.reshape((test_X.shape[0], n_hours*n_features))
    # invert scaling for forecast
    inv_yhat = np.concatenate((yhat, test_X[:, -7:]), axis=1)
    inv_yhat = scaler.inverse_transform(inv_yhat)
    inv_yhat = inv_yhat[:,0]

    # invert scaling for actual
    test_y = test_y.reshape((len(test_y), 1))
    inv_y = np.concatenate((test_y, test_X[:, -7:]), axis=1)
    inv_y = scaler.inverse_transform(inv_y)
    inv_y = inv_y[:,0]

    # calculate RMSE
    print("calculate RMSE ...")
    rmse = math.sqrt(mean_squared_error(inv_y, inv_yhat))
    print('Test RMSE: %.3f' % rmse)

    print("plot_predictions")
    pyplot.plot(inv_y,    label='inv_y')
    pyplot.plot(inv_yhat, label='inv_yhat')
    pyplot.legend()
    pyplot.show()


def main():
    print("==============================================================================================")
    print("=================  Multivariate Time Series Forecasting with LSTMs in Keras  =================")
    print("==============================================================================================")
    print("Source: https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/")
    print("______________________________________________________________________________________________")

    # TODOTODO: Agregar parametros

    # TODOTODO: Usar PLOTLY


    ######################################
    ## PARAMETERS 
    ######################################
    original_data_set_file = "C:\\datasets\\air_pollution_beijing\\PRSA_data_2010.1.1-2014.12.31.csv"

    ######################################

    filename_preprocess = load_data(original_data_set_file)
    print("filename_preprocess = " + filename_preprocess)

    print("show_data ...")
    show_data(filename_preprocess)

    print("lstm_core ...")
    lstm_core(filename_preprocess)


    print("DONE!")
if __name__ == "__main__":
    main()