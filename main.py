from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import Response

# import mh_z19 as sensor
import time
import calendar
import json

class sensorClass: 
    async def read(self):
        return "{}"

sensor = sensorClass()

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/fetch-co2", methods = ["GET"])
async def get_data():
    try:
        co2 = await sensor.read()
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        data = json.dumps({data: co2, "time_stamp": time_stamp})
        return Response(response=data, status=200, mimetype='application/json')
    except Exception as e:
        print(e)
        return jsonify({'error': "Something went wrong"}), 400