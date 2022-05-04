# code for your API
from ctypes import util
from urllib import response
from flask import Flask, request, jsonify
import server.util as util

app = Flask(__name__)

@app.route('/location_names')
def get_location_names():
    response = jsonify({
        "locations": util.get_location_names
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("start flask server!!!")
    app.run()