import pickle
import json
import numpy as np

__features = None
__locations = None
__model = None




def get_estimated_price(location,number_of_bedrooms, living_area, surface_area_land,pool,condition):
    try:
        loc_index = __locations.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__features) + len(__locations))
    x[0] = number_of_bedrooms
    x[1] = living_area
    x[2] = surface_area_land
    x[3] = pool
    x[4] = condition

    if loc_index>=0:
        x[loc_index] = 1

    
    # print(len(__features) + len(__locations))
    return round(__model.predict([x])[0])




def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts")
    
    global __locations
    global __features

    try:
        with open('./model/columns.json', 'r') as f:
            json_loaded = json.load(f)
            __locations = json_loaded['locations']
            __features = json_loaded['features']
    except:
        FileNotFoundError

    global __model
    if __model is None:
        with open('./model/model_lg.pkl', 'rb') as f:
            __model = pickle.load(f)
        print("loading saved artifacts...done")


    
if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_estimated_price('Gent', 2, 150, 200, True, 3))
    # print(get_estimated_price('Verviers', 2, 150, 200, True, 4))
