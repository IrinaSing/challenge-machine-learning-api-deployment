import pickle
import json
import numpy as np

__features = None
__locations = None
__condition = None
__model = None




def get_estimated_price(location,number_of_bedrooms, living_area, furnished, open_fireplace, terrace, garden, surface_area_land,pool,condition):
    try:
        loc_index = __locations.index(location.lower())
    except:
        loc_index = -1

    try:
        cond_index = __condition.index(condition.lower())
    except:
        cond_index = -1

    x = np.zeros(len(__features) + len(__condition) + len(__locations))
    x[0] = number_of_bedrooms
    x[1] = living_area
    x[2] = furnished
    x[3] = open_fireplace
    x[4] = terrace
    x[5] = garden
    x[6] = surface_area_land
    x[7] = pool

    if loc_index>=0:
        x[loc_index] = 1

    if cond_index>=0:
        x[cond_index] = 1
    
    return round(__model.predict([x])[0],2)




def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts")
    
    global __locations
    global __features
    global __condition

    with open("./model/columns.json", 'r') as f:
        json_loaded = json.load(f)
        __locations = json_loaded['locations']
        __features = json_loaded['features']
        __condition = json_loaded['condition']

    global __model
    if __model is None:
        with open('./model/model_lg.pkl', 'rb') as f:
            __model = pickle.load(f)
        print("loading saved artifacts...done")


    
if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_estimated_price('Gent', 3, 200, False, False, True, True, 200, False, 'as_new'))
    #print(get_estimated_price('Gent', 3, 300, True, False, False, True, 100, False, 'to_renovate'))
