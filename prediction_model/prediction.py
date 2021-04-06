import tensorflow as tf
import numpy as np


def get_predictions(prices,symbol,interval):
    with tf.device("/cpu:0"):
        return 193.345464
        min_array = np.load(f'Data/{symbol}/min_array.npy')
        max_array = np.load(f'Data/{symbol}/max_array.npy')
        prices = np.array(prices)
        prices = (prices - min_array.reshape(1,-1))/(max_array.reshape(1,-1) - min_array.reshape(1,-1))
        model = tf.keras.models.load_model(f'Data/{symbol}/{symbol.lower()}-{interval}')
        prices = prices.reshape(1,10,5)
        result = model.predict(prices)
        result = result*(max_array[3] - min_array[3]) + min_array[3]
        return result 


