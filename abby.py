import json
import numpy as np
import pickle

def savedvals():
    global data
    global sub
    global ml_model


    with open("./model/columns.json", "r") as f:
        data = json.load(f)['data']
        sub = data[4:]

    with open("./model/PriceNEW.pickle", "rb") as f:
        ml_model = pickle.load(f)


def price(suburbs,bedroom2,bathroom,car,buildingarea):
    try:
        ptr = data.index(suburbs)

    except:
        ptr = -1

    a = np.zeros(len(data))
    a[0] = bedroom2
    a[1] = bathroom
    a[2] = car
    a[3] = buildingarea
    if ptr >= 0:
        a[ptr] = 1

    return round(ml_model.predict([a])[0], 3)


def suburbs():
    return sub




if __name__ == "__main__":
    savedvals()
    print(suburbs())
    print(price('abbotsford',2, 1,0,79))


