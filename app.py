# code for your API
from urllib import response
from flask import Flask, request, jsonify, render_template
from predict import prediction as prediction

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("app.html")

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
    surface_area_land = float(request.form['surface_area_land'])
    pool = bool(request.form['pool'])
    condition = int(request.form['condition'])

    response = jsonify({
        'estimated_price': prediction.get_estimated_price(location,number_of_bedrooms, living_area, surface_area_land,pool, condition)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("start flask server")
    prediction.load_saved_artifacts()
    app.run()