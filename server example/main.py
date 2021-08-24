from flask import Flask, request
import time
from FedinCode import Auction
import threading
import atexit
import numpy as np
import pandas as pd
import asyncio
import traceback
from random import uniform
import os


auction = Auction()
dict_dunch_auction = {}
list_id_dutch = []
try:
    df_sell = pd.DataFrame({})
    df_buy = pd.DataFrame({})
    df_sell.to_csv('dfsell.csv', sep='\t')
    df_buy.to_csv('dfbuy.csv', sep='\t')
except:
    pass
    # print('(((')
app = Flask(__name__)
df_sell = pd.DataFrame(columns=['bet', 'lot', 'time', 'id'])
# df_sell = pd.DataFrame({'id':0, 'bet':0, 'time':0, 'lot':0})
df_buy = pd.DataFrame(columns=['bet', 'lot', 'time', 'id'])

# df_buy = pd.DataFrame({'id':0, 'bet':0, 'time':0, 'lot':0})
# args = {"args": [
#     "run",
#     "--no-reload"]}
# # app.run(args['args'])
# app.config=args


# con_sell = sqlite3.connect('sell.db')
# cursor_sell = con_sell.cursor()
# cursor_sell.execute('''CREATE TABLE IF NOT EXISTS sell(id INTEGER, bet FLOAT, time FLOAT, lot FLOAT)''')

# con_buy = sqlite3.connect('buy.db')
# con_sell = sqlite3.connect('sell.db')

def df_add_bets_sell(id_, bet, times, lot):
    df_sell.loc[str(df_sell.shape[0] + 1)] = [bet, lot, int(times), id_]
    df_sell.to_csv('dfsell.csv', sep='\t')



def df_add_bets_buy(id_, bet, times, lot):
    df_buy.loc[str(df_sell.shape[0] + 1)] = [bet, lot, int(times), id_]
    df_buy.to_csv('dfbuy.csv', sep='\t')
# def add_bets_sell(id_, bet, times, lot):
#     cursor_sell.execute("INSERT INTO sell (id, bet, time, lot) VALUES  ('%d', '%f', '%f', '%f')" % (id_, bet, times, lot))
#     con_sell.commit()


# con_buy = sqlite3.connect('buy.db')
# cursor_buy = con_buy.cursor()
# cursor_buy.execute('''CREATE TABLE IF NOT EXISTS buy(id INTEGER, bet FLOAT, time FLOAT, lot FLOAT)''')


# def add_bets_buy(id_, bet, times, lot):
#     cursor_buy.execute("INSERT INTO buy (id, bet, time, lot) VALUES  ('%d', '%f', '%f', '%f')"%(id_, bet, times, lot))
#     con_buy.commit()


@app.route('/<int:id_>/new_lot_sell/<float:cost>/<float:v>/', methods=['GET', 'POST'])
@app.route('/<int:id_>/new_lot_sell/<int:cost>/<float:v>/', methods=['GET', 'POST'])
@app.route('/<int:id_>/new_lot_sell/<float:cost>/<int:v>/', methods=['GET', 'POST'])
@app.route('/<int:id_>/new_lot_sell/<int:cost>/<int:v>/', methods=['GET', 'POST'])
def new_lot_sell(id_, cost, v):
    times = time.time()
    if request.method == "POST":
        df_add_bets_sell(id_=id_, bet=cost, times=float(times), lot=v)
        return 'ok'
    else:
        df_add_bets_sell(id_=id_, bet=cost, times=float(times), lot=v)
        return 'ok'


@app.route('/<int:id_>/new_lot_buy/<float:cost>/<float:v>/', methods=['GET', 'POST'])
@app.route('/<int:id_>/new_lot_buy/<int:cost>/<float:v>/', methods=['GET', 'POST'])
@app.route('/<int:id_>/new_lot_buy/<float:cost>/<int:v>/', methods=['GET', 'POST'])
@app.route('/<int:id_>/new_lot_buy/<int:cost>/<int:v>/', methods=['GET', 'POST'])
def new_lot_buy(id_, cost, v):
    times = time.time()
    if request.method == "POST":
        df_add_bets_buy(id_=id_, bet=cost, times=times, lot=v)
        return 'ok'
    else:
        df_add_bets_buy(id_=id_, bet=cost, times=times, lot=v)
        return 'ok'


@app.route('/')
def index():
    return 'q'


async def start_auction():
    global df_buy, df_sell
    # time.sleep(second)
    # print('-------')
    try:
        while True:
            try:
                # print('---------')
                #print(df_sell[:], df_buy[:], sep='\n')
                second = 60
                await asyncio.sleep(second)
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
                traceback.print_exc()
                # print('error in auction')
    except:
        traceback.print_exc()
        # print('bruh')
    finally:
        # print(df_sell[:])
        # print(df_buy[:])dfsell
        # try:
        #     # df_sell.drop(axis=0, inplace=True)
        #     # df_buy.drop(axis=0, inplace=True)
        # except ValueError:
        #     print("bruuuh")
        # finally:
        #     print("не вошло")
        pass
    t1 = threading.Timer(second, start_auction)
    t1.start()



def exit_handler():
    try:
        # print(123456789)
        # t1.join()
        # t2.join()
        # t3.join()
        df_sell.drop(axis=0, inplace=True)
        df_buy.drop(axis=0, inplace=True)
        t4.join()
    except NameError:
        pass

@app.route('/sos/<int:id_>/<float:lot>', methods=['GET', 'POST'])
@app.route('/sos/<int:id_>/<int:lot>', methods=['GET', 'POST'])
def start_DutchAuction(id_, lot):
    global dict_dunch_auction
    if request.method == "POST":
        # запустить совметсную (DutchAuctionBet.py)
        # global dict_dunch_auction
        dict_dunch_auction[id_] = str(lot)
        return 'ok'
    else:
        dict_dunch_auction[id_] = str(lot)
        return 'ok'

@app.route('/<int:id_>/sos/list', methods=['GET', 'POST'])
def sos_list(id_):
    global dict_dunch_auction
    if request.method == "POST":
        if id_ in dict_dunch_auction.keys():
            return list_id_dutch
        else:
            return ' '.join(dict_dunch_auction.values())
    else:
        # global dict_dunch_auction
        if id_ in dict_dunch_auction.keys():
            return list_id_dutch
        else:
            return ' '.join(dict_dunch_auction.values())

@app.route('/<int:id_>/graph', methods=['GET', 'POST'])
def graph(id_):
    if request.method == "POST":

        try:
            return dct
        except NameError:
            dct = dict()
            d = 51
            x_values1 = np.array([int(i) for i in range(d)], dtype=float).tolist()
            y_values1 = np.array([uniform(4, 7) for i in range(d)], dtype=float)
            # y_values = np.array([1 for i in range(d)]).tolist()
            for i in range(d):
                dct[x_values1[i]] = y_values1[i]
            return dct
    else:
        try:
            return dct
        except NameError:
            dct = dict()
            d = 51
            x_values1 = np.array([int(i) for i in range(d)], dtype=float).tolist()
            y_values1 = np.array([uniform(0, 7) for i in range(d)], dtype=float)
            # y_values = np.array([1 for i in range(d)]).tolist()
            for i in range(d):
                dct[x_values1[i]] = y_values1[i]
            return dct



# def start_server():
#     if __name__ == "__main__":
#         threading.Thread(target=app.run).start()
#         # app.run(use_reloader=False)

if __name__ == "__main__":
    threading.Thread(target=app.run).start()

def exit():
    atexit.register(exit_handler)

# print('2222')
t4 = threading.Thread(target=exit(), args=())
# t1 = threading.Thread(target=os.system, args=('python запускай_отсюда.py',))
# t2 = threading.Thread(target=os.system, args=('python startAgent2.py',))
# t8 = threading.Thread(target=os.system, args=('python startAgent3.py',))
# t9 = threading.Thread(target=os.system, args=('python startAgent4.py',))
# t10 = threading.Thread(target=os.system, args=('python startAgent5.py',))
# t11 = threading.Thread(target=os.system, args=('python startAgent26.py',))
# t12 = threading.Thread(target=os.system, args=('python startAgent27.py',))
# t13 = threading.Thread(target=os.system, args=('python startAgent8.py',))
# t1.start()
# t2.start()
# t8.start()
# t9.start()
# t10.start()
# t11.start()
# t12.start()
# t13.start()
# t2 = threading.Thread(target=start_server(), args=())
# print('11111')
asyncio.run(start_auction())
# t3 = threading.Timer(180, start_auction, args=())
# for thread in threading.enumerate():
#     print(thread.name)
# t3.start()
t4.start()
# t2.start()

# print('123456789789456123')