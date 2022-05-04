from copyreg import pickle
import json

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[7:]

    with open("./artifacts/model_lg.pickle", 'rb') as m:
        __model = pickle.load(m)
        print("loading the artifacts is done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())