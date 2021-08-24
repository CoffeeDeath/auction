# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:08:50 2021

@author: user
"""
import numpy as np

alphas = [1]
hiddenSize = 64

# подсчитаем нелинейную сигмоиду
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# преобразуем результат сигмоиды к производной
def sigmoid_output_to_derivative(output):
    return output*(1-output)
    
X = np.array()
y = np.array().T
for alpha in alphas:
    np.random.seed(1)

    # randomly initialize our weights with mean 0
    synapse_0 = 2*np.random.random((10,hiddenSize)) - 1
    synapse_1 = 2*np.random.random((hiddenSize,1)) - 1

    for j in range(60000):

        # Прямое распространение по уровням 0, 1 и 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0,synapse_0))
        layer_2 = sigmoid(np.dot(layer_1,synapse_1))

        # как сильно ошиблись?
        layer_2_error = layer_2 - y

        if (j% 10000) == 0:
            print ("Ошибка после "+str(j)+" повторений:" + str(np.mean(np.abs(layer_2_error))))
            print(synapse_0)
        # в каком направлении цель?
        # уверены ли мы? Если да, то не нужно слишком сильных изменений
        layer_2_delta = layer_2_error*sigmoid_output_to_derivative(layer_2)

        # насколько каждое значение из l1 влияет на ошибку в l2 (в соответствии с весами)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # в каком направлении цель l1?
        # уверены ли мы? Если да, то не нужно слишком сильных изменений
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)

        synapse_1 -= alpha * (layer_1.T.dot(layer_2_delta))
        synapse_0 -= alpha * (layer_0.T.dot(layer_1_delta))
            