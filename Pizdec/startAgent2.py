import random
import threading
from Agent import Agent
import numpy as np
from random import uniform, randint
from time import time, ctime, sleep
from startMain import query

URL = 'http://193.32.219.22:5000/'
# id_ = randint(100_000, 999_999)
id_ = '222222'
d = 51
y_values = np.array([uniform(-1, 1) for i in range(d)], dtype=float)
x_values = np.array([i for i in range(d)], dtype=float)
d1 = 51
# y_values1 = np.array([uniform(0, 7) for i in range(d)], dtype=float)
values = query('222222')

# рандом значений


graph, prices = Agent(id_=id_, url=URL, pow=20).Graph(x_values=x_values, y_values=y_values, d=d, x_values1=values[0], y_values1=values[1], d1=d1)

a = Agent(id_=id_, url=URL, graph=graph, prices=prices)
# times =
while True:
    # print(f'time: {time()}')
    time_ = ctime(time()).split()[3].split(':')
    # print(time_)
    time_ = list(map(int, time_))
    # print(f'list time: {time_}')
    time_ = ((time_[0] * 3600) + (time_[1] * 60) + time_[2]) / 1728
    # print(time_)
    a.Check(time=time_)
    # print('-------------')
    sleep(45)