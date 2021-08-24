from flask import Flask
import numpy as np
from random import uniform


app = Flask(__name__)

@app.route('/')
def index():

    try:
        return dct
    except NameError:
        dct = dict()
        d = 51
        x_values1 = np.array([i for i in range(d)], dtype=float)
        for i in range(d):
            dct[x_values1[i]] = 1
        return dct


if __name__ == '__main__':
    app.run(debug=True)
    # print('id:', a.id)
