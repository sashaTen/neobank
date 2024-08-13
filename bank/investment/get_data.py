import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense


# data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
def forecast(tickle , start , end , window ,  days_to_forecast):
    data = yf.download(tickle, start=start, end=end)
    predictions =  lstm_model(data['Close'].values , window ,  days_to_forecast)
    return predictions
     


def prepare_stock_data(price_data, sequence_length, forecast_days):

    price_data = price_data[~np.isnan(price_data)]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(price_data.reshape(-1, 1))

    x_data, y_data = [], []
    for i in range(sequence_length, len(scaled_data) - forecast_days):
        x_data.append(scaled_data[i-sequence_length:i, 0])
        y_data.append(scaled_data[i + forecast_days, 0])  # Predicting 3 days ahead

    x_data, y_data = np.array(x_data), np.array(y_data)
    x_data = np.reshape(x_data, (x_data.shape[0], x_data.shape[1], 1))

    # Split into training and testing sets
    train_size = int(len(x_data) * 0.8)
    x_train, x_test = x_data[:train_size], x_data[train_size:]
    y_train, y_test = y_data[:train_size], y_data[train_size:]

    return x_train, x_test, y_train, y_test

def lstm_model(price_data, sequence_length,days_to_forecast, epochs=25, batch_size=32):

    # Preprocess the data
    x_train, x_test, y_train, y_test = prepare_stock_data(price_data, sequence_length, days_to_forecast)

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    # Train the model
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)
    predictions = model.predict(x_test)
    return  predictions


#predictions =  lstm_model(data['Close'].values , 30 ,  3)
#predictions  = forecast("AAPL", "2020-01-01", "2021-01-01" , 40  , 3)
