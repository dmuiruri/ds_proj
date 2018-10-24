
import requests # http://docs.python-requests.org/en/master/
import json     # https://docs.python.org/3/library/json.html
import data_manager as dm
import pandas as pd


PREDICT_API_URL = 'http://127.0.0.1:5000/predict'
REQUEST_HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


# TODO: construct a payload for the prediction POST request
#consumption_json = pd.DataFrame(dm.get_industrial_electricity_data()).to_json()
#weather_json = dm.get_weather_data().to_json()
#data = {'consumption': consumption_json, 'weather': weather_json, 'message': 'Dadaa'}

# make the POST
#response = requests.post(PREDICT_API_URL, data=json.dumps(data), headers=REQUEST_HEADERS)

# test with GET request
response = requests.get(PREDICT_API_URL)

# json response
print('Response from server:', response.text)

