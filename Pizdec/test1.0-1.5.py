from flask import Flask
import pandas as pd
from flask_classful import FlaskView, route
from random import randint
# from AnGraph import Holy_Grail

app = Flask(__name__)


class DutchAuctionServer(FlaskView):

    def __init__(self, cost=100, step_cost=1, lot=0, id=100):
        self.id = id
        self.cost, self.step_cost, self.lot = cost, step_cost, lot

        self.name_file = '../out.csv'
        self.write_data(pd.DataFrame({'id': [100], 'cost': [1000], 'step_cost': [1], 'lot': [500]}))

        # data_dict = {'id': [self.id], 'cost': [self.cost], 'step_cost': [self.step_cost], 'lot': [self.lot]}
        # self.df = pd.DataFrame(data_dict)
        # print(self.id)


    def write_data(self, df):
        df.to_csv('out.csv', sep='\t', encoding='utf-8', index=False)

    def read_csv(self):
        df = pd.read_csv('../out.csv', sep='\t', encoding='utf-8')
        return df

    @route('/')
    def index(self):
        return 'ok'

    @route('/auctionid')
    def my_auction_id(self):
        return str(self.id)

    @route('/<int:auc_id>/cost/')
    def now_cost(self, auc_id):
        df = self.read_csv()
        return str(df.loc[df['id'].tolist().index(auc_id)]['cost'])
        # print(self.df[:])
        # return str(self.df.loc[self.df['id'].tolist().index(id)]['cost'])

    @route('/<int:id>/cost/isBuy')
    def isBuy(self, id):
        df = self.read_csv()
        df.drop(df.index[df['id'] == id])
        self.write_data(df)
        # self.df = self.df.drop(self.df.index[self.df['id'] == id])  # , inplace=True)
        # print(self.df[:])
        return 'auction is closed'

    # @route('/<int:id>/step_cost/')
    # def step(self, id):
    #     # new_price = self.df.loc[self.df['id'].tolist().index(id)]['cost'] - \
    #     #             self.df.loc[self.df['id'].tolist().index(id)]['step_cost']
    #     # self.df.at[self.df['id'].tolist().index(id), 'cost'] = new_price
    #     return 'ok'


a = DutchAuctionServer(cost=1000, step_cost=1, lot=100, id=randint(100_000, 999_999))
a.register(app, route_base='/')
if __name__ == '__main__':
    app.run(debug=True)
    print('id:', a.id)
