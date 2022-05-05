# code for your API
#from ctypes import util
from urllib import response
from flask import Flask, request, jsonify
import predict.prediction as prediction

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hi"

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': prediction.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    location = request.form['location']
    number_of_bedrooms = int(request.form['number_of_bedrooms'])
    living_area = float(request.form['living_area'])
    furnished = bool(request.form['furnished'])
    open_fireplace = bool(request.form['open_fireplace'])
    terrace = bool(request.form['terrace'])
    garden = bool(request.form['garden'])
    surface_area_land = float(request.form['surface_area_land'])
    pool = bool(request.form['pool'])
    condition = request.form['condition']

    response = jsonify({
        'estimated_price': prediction.get_estimated_price(location,number_of_bedrooms, living_area, furnished, open_fireplace, terrace, garden, surface_area_land,pool, condition)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("start flask server")
    prediction.load_saved_artifacts()
    app.run()