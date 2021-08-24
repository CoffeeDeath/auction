# import sys
from random import randint
import pandas as pd


class Auction():

    def __init__(self):
        self.buy, self.sell = [], []
        self.result, self.allbuy = [], []
        self.recomend_buy, self.recomend_sell = [], []

    def AppendBuy(self, y):
        y[2] = int(float(y[2]))
        y[2] = -y[2]
        self.buy.append(y)
        self.buy.sort()
        # print(self.buy)
        for j in self.buy:
            j[2] = abs(j[2])
        # print(f'sorted list (buy): {self.buy}')

    def AppendSell(self, y):
        y[0], y[2] = int(float(y[0])), int(float(y[2]))
        y[0], y[2] = -y[0], -y[2]
        self.sell.append(y)
        self.sell.sort()
        # print(self.sell)
        for j in self.sell:
            j[0], j[2] = abs(j[0]), abs(j[2])

        # print(f'sorted list (sell): {self.sell}')
    #
    # def DeleteSell(self, k):
    #     del self.sell[self.sell.index(k)]
    #
    # def DeleteBuy(self, k):
    #     del self.buy[self.buy.index(k)]
    #

    def DelElement(self, lst, k):
        del lst[lst.index(k)]
        return lst

    def start_of_sales(self):
        # print('-----------------')
        df_sell = pd.read_csv('dfsell.csv', sep='\t')
        df_buy = pd.read_csv('dfbuy.csv', sep='\t')
        self.sell = df_sell.astype(float).values.tolist()
        self.buy = df_buy.astype(float).values.tolist()

        if self.buy[-1][1] > self.sell[-1][1]:
            try:
            # print(1)
                if len(self.buy) == 1:
                    print(int(self.buy[-1][3]), 'купил', self.sell[-1][1], 'Квт у', int(self.sell[-1][3]), 'за',
                          max(self.buy[-2][0], self.sell[-1][0]), 'руб')
                else:
                    print(int(self.buy[-1][3]), 'купил', self.sell[-1][1], 'Квт у', int(self.sell[-1][3]), 'за',
                          max(self.buy[-1][0], self.sell[-1][0]), 'руб')
            except IndexError:
                print('error', 'IndexError', 'in FedinCode')
            self.buy[-1][1] -= self.sell[-1][1]
            self.sell = self.DelElement(self.sell, self.sell[-1])
        elif self.buy[-1][1] == self.sell[-1][1]:
            # print(2)
            if len(self.buy) == 1:
                print(int(self.buy[-1][3]), 'купил', self.sell[-1][1], 'Квт у', int(self.sell[-1][3]),
                      'за', self.buy[-1][0], 'руб')
            else:
                print(int(self.buy[-1][3]), 'купил', self.sell[-1][1], 'Квт у', int(self.sell[-1][3]), 'за',
                      max(self.buy[-2][0], self.sell[-1][0]), 'руб')
            self.sell = self.DelElement(self.sell, self.sell[-1])
            self.buy = self.DelElement(self.buy, self.buy[-1])
        else:
            # print(3)
            if len(self.buy) == 1:
                print(int(self.buy[-1][3]), 'купил', self.buy[-1][1], 'Квт у', int(self.sell[-1][3]),
                      'за', self.buy[-1][0], 'руб')
            else:
                print(int(self.buy[-1][3]), 'купил', self.buy[-1][1], 'Квт у', int(self.sell[-1][3]), 'за',
                      max(self.buy[-2][0], self.sell[-1][0]), 'руб')
            self.sell[-1][1] -= self.buy[-1][1]
            self.buy = self.DelElement(self.buy, self.buy[-1])
            self.recomend_buy, self.recomend_sell = self.buy, self.sell
            # self.sell
        df_sell = pd.DataFrame(self.sell, index=[i for i in range(len(self.sell))])
        df_buy = pd.DataFrame(self.buy, index=[i for i in range(len(self.buy))])
        df_sell.to_csv('dfsell.csv', sep='\t')
        df_buy.to_csv('dfbuy.csv', sep='\t')
        return [self.buy, self.sell]

    def start_price_recommendations(self, a, b):
        self.recomend_buy, self.recomend_sell = a, b
        try:
            if self.recomend_buy[-1][1] > self.recomend_sell[-1][1]:
                self.result.append((self.recomend_buy[-1][3], (self.recomend_sell[-1][0] + self.recomend_buy[-1][0]) / 2))
                while self.recomend_sell and self.recomend_buy[-1][1] > self.recomend_sell[-1][1]:
                    self.recomend_buy[-1][1] -= self.recomend_sell[-1][1]
                    self.result.append((self.recomend_sell[-1][3], (self.recomend_sell[-1][0] + self.recomend_buy[-1][0]) / 2))
                    self.recomend_sell = self.DelElement(self.recomend_sell, self.recomend_sell[-1])
                self.recomend_buy = self.DelElement(self.recomend_buy, self.recomend_buy[-1])
            elif self.recomend_buy[-1][1] < self.recomend_sell[-1][1]:
                self.allbuy = []
                while self.recomend_buy and self.recomend_buy[-1][1] < self.recomend_sell[-1][1]:
                    self.recomend_sell[-1][1] -= self.recomend_buy[-1][1]
                    self.allbuy.append(self.recomend_buy[-1][3])
                    pop = self.recomend_buy.pop()
                    for elem in self.allbuy:
                        self.result.append((elem, (self.recomend_sell[-1][0] + pop[0] / 2)))
            elif self.recomend_buy[-1][1] == self.recomend_sell[-1][1]:
                self.result.append((self.recomend_buy[-1][3], (self.recomend_sell[-1][0] + self.recomend_buy[-1][0]) / 2))
                self.result.append((self.recomend_sell[-1][3], (self.recomend_sell[-1][0] + self.recomend_buy[-1][0]) / 2))
                self.recomend_buy = self.DelElement(self.recomend_buy, self.recomend_buy[-1])
                self.recomend_sell = self.DelElement(self.recomend_sell, self.recomend_sell[-1])
            print(self.result)
            return self.result
        except IndexError:
            return [['error', 'IndexError', 'in FedinCode']]



# a = Auction()
#
# for i in range(1000):
#     x = ['s', randint(2, 6), randint(1, 10), randint(1, 21), i + 1001]
#     # print(x)
#     a.AppendSell(x[1:])
#
# for i in range(1000):
#     x = ['b', randint(2, 6), randint(1, 10), randint(1, 21), i + 1]
#     a.AppendBuy(x[1:])
# print('random')
# # print(a.start_price_recommendations(*a.start_of_sales()))
# lst = list('всё купили')
# lst_ = []
# while a.buy and a.sell and a.buy[-1][0] >= a.sell[-1][0]:
#     lst_ = a.start_of_sales()
# print(lst_, len(lst_[0]), len(lst_[1]), sep='\n')
# while a.recomend_buy and a.recomend_sell:
#     lst = a.start_price_recommendations(*lst_)
#
# print(lst)
