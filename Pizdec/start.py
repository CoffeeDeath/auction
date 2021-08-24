import time
import pandas as pd
from main import *

def start_auction():
    # global df_buy, df_sell
    try:
        df_buy = pd.read_csv('dfbuy.csv', sep='\t')
        df_sell = pd.read_csv('dfsell.csv', sep='\t')
    except:
        pass
    # time.sleep(second)
    print('-------')
    try:
        try:
            second = 60
            time.sleep(second)
            # sell, buy = [], []
            # try:
            # row = df_sell.astype(str).values.tolist()
            # print(row)
            for i in df_sell.astype(float).values.tolist():
                auction.AppendSell(i)
            for i in df_buy.astype(float).values.tolist():
                # row = df_buy.astype(str).values.tolist()
                # dor
                auction.AppendBuy(i)

            lst_ = []
            lst = []
            while auction.buy and auction.sell and auction.buy[-1][0] >= auction.sell[-1][0]:
                lst_ = auction.start_of_sales()
            # print(lst_, len(lst_[0]), len(lst_[1]), sep='\n')

            while auction.recomend_buy and auction.recomend_sell:
                lst = auction.start_price_recommendations(*lst_)
                print(lst[-1])
        except:
            # traceback.print_exc()
            print('error in auction')
    except:
        traceback.print_exc()
        print('bruh')
    # finally:
        # print(df_sell[:])
        # print(df_buy[:])

while True:
    start_auction()
