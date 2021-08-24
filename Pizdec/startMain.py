import requests

def query(id_):
    URL = f'http://127.0.0.1:5000/{id_}/graph'


    r = requests.get(URL)
    if not r.ok:
        query(id_)
    r = dict(r.json())
    # print(r)

    x_values = [float(i) for i in r.keys()]
    y_values = [float(i) for i in r.values()]
    # print(x_values, y_values, sep='\n')
    return [x_values, y_values]