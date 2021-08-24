import pandas as pd
from threading import Timer
import atexit
import time


def write_data(name_file, df):
    df.to_csv(name_file, sep='\t', encoding='utf-8', index=False)


def read_csv(name_file):
    df = pd.read_csv(name_file, sep='\t', encoding='utf-8')
    return df


def exit_handler():
    try:
        t1.join()
    except NameError:
        pass

second = 5

def step():
    global t1
    second = 2
    try:
        t1.join()
    except NameError:
        df = read_csv('../out.csv')
        for i in df['id'].tolist():
            # print(1)
            a = df.loc[df['id'].tolist().index(i)]['cost'] - \
                df.loc[df['id'].tolist().index(i)]['step_cost']
            if a > 0:
                df.loc[df['id'].tolist().index(i)]['cost'] = a
        write_data('../out.csv', df)
        print(df[:])

        # df.drop(axis=0, inplace=True)
        time.sleep(second)

        t1 = Timer(second, step())
        t1.start()
    except pd.errors.EmptyDataError:
        pass


atexit.register(exit_handler)

step()
