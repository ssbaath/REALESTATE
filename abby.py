import json
import numpy as np
import pickle


__locations = None
__data_columns = None
__model = None

def price_estimate(suburbs,bedroom2,bathroom,car,buildingarea):
    try:
        loc_index = __data_columns.index(suburbs.lower())
    except:
        loc_index = -1

    a = np.zeros(len(__data_columns))
    a[0] = bedroom2
    a[1] = bathroom
    a[2] = car
    a[3] = buildingarea
    if loc_index >= 0:
        a[loc_index] = 1

    return round(__model.predict([a])[0], 3)

def get_location_names():
    return __locations

def load_saved_artifcats():
    print("loading saved artifacts...start")
    global __data_columns
    global __model
    global __locations


    with open("./model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]

    with open("./model/HousingPrice.pickle", "rb") as f:
        __model = pickle.load(f)
        print("loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifcats()
    print(get_location_names())
    print(price_estimate('abbotsford',2, 1,0,79))


