from AnGraph import Holy_Grail
import requests


class Agent(Holy_Grail):
    def __init__(self, id_, url, **kwargs) -> None:
        self.url = url
        self.id_ = id_
        self.data = kwargs
        # print(self.data)
        try:
            super().__init__(self.data['pow'])
        except KeyError:
            pass
        # input('Введите город: ')

    def Buy(self, how, price):
        # abc = requests.request(f'{self.url}/{self.id_}/new_lot_buy/{price}/{how}/')

        url_ = f'{self.url}{self.id_}/new_lot_buy/{price}/{how}/'
        print(url_)
        abc = requests.request('GET', url=url_)
        print(abc)
        # print('Покупка', how, 'По цене', price)

    def Sell(self, how, price):
        url_ = f'{self.url}{self.id_}/new_lot_sell/{price}/{how}/'
        print(url_)
        abc = requests.request('GET', url=url_)
        print(abc)
        # from Price import MinSellPrice
        # Выставить энергию с ценой MinSellPrice(kargs)
        # print('Продажа', how, 'По цене', price)

    def Graph(self, y_values, x_values, d, x_values1, y_values1, d1):
        # pow - заярд аккум
        # from AnGraph import Holy_Grail
        # import numpy as np
        # from random import uniform
        # # d = 51
        # # y_values = np.array([uniform(-1, 1) for i in range(d)], dtype=float)
        # # x_values = np.array([i for i in range(d)], dtype=float)

        return Holy_Grail.main(self, y_values=y_values,  x_values=x_values, d=d, x_values1=x_values1,
                               y_values1=y_values1, d1=d1)

    # два массива (массив продажи и покупки ['продажа', проценты сколько надо, время начала промежутка графика, время конца промежутка графика, время промежутка)
    # (двумерный массив[цена])

    def Check(self, time):
        k = 0
        k1 = 0
        for i in range(len(self.data['prices'])):
            for j in range(len(self.data['prices'][i])):
                # print(self.data['graph'][k1][4])
                # print(self.data['graph'][k1][6])
                # print(self.data['graph'][k1][0])
                if self.data['graph'][k1][4] <= time <= self.data['graph'][k1][6]:
                    if self.data['graph'][k1][0] == 'Покупка':
                        self.Buy(self.data['graph'][k1][1], self.data['prices'][i][j])
                    else:
                        self.Sell(self.data['graph'][k1][1], self.data['prices'][i][j])
                k1 += 1
            k += 1

