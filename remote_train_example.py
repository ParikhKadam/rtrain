#!/usr/bin/env python3

import numpy
import rtrain.client
import sys

from keras.models import Sequential
from keras.layers import Dense

if __name__ == '__main__':
    model = Sequential([
        Dense(512, activation='tanh', input_shape=(2, )),
        Dense(1),
    ])

    x_train = numpy.random.randn(1000, 2)
    y_train = numpy.matrix(
        numpy.sqrt(x_train[:, 0]**2 + x_train[:, 1]**2)).transpose()

    session = rtrain.client.RTrainSession("http://lachlan:foo@127.0.0.1:5000")
    trained_model = session.train(model, 'mean_squared_error', 'rmsprop',
                                  x_train, y_train, 10, 16384)
    if trained_model is None:
        print("Error training model.", file=sys.stderr)
        sys.exit(1)

    print(numpy.sqrt(0.3**2 + 0.6**2))
    print(trained_model.predict(numpy.matrix([[0.3, 0.6]]))[0, 0])
