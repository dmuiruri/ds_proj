import requests # http://docs.python-requests.org/en/master/

import data_manager as dm

'''
(Test) client script for the electricity consumption forecast API

'''


IC_PREDICT_API_URL_LOCAL  = 'http://127.0.0.1:5000/predict/industry'
HELLO_API_URL_LOCAL    = 'http://127.0.0.1:5000/hello'
HELLO_API_URL_HEROKU   = 'https://ds-2018-webapi.herokuapp.com/hello'
IC_PREDICT_API_URL_HEROKU = 'https://ds-2018-webapi.herokuapp.com/predict/industry'


# Construct the payload for the prediction POST request, payload contains 
# consumption and weather data.
# Ask the data from data_manager and convert to csv for the POST request.
# Can't put the dataframes directly to the request, but the CSV format works.
# weather_df = dm.get_ic_weather()
# consumption_df = dm.get_industrial_electricity_data()
# forecast_base_data = [('files', consumption_df.to_csv()), ('files', weather_df.to_csv())]


# Do the POST to the server NO POST anymore
#response = requests.post(PREDICT_API_URL_LOCAL, files=forecast_base_data)
#response = requests.post(PREDICT_API_URL_HEROKU, files=forecast_base_data)

# Some GET requests for a sanity check
#response = requests.get(HELLO_API_URL_LOCAL)
#response = requests.get(HELLO_API_URL_HEROKU)
response = requests.get(IC_PREDICT_API_URL_LOCAL) # this url has also a GET handler
#response = requests.get(IC_PREDICT_API_URL_HEROKU) # this url has also a GET handler

# Print the server response. 
# The response would contain the electricity consumption forecast, maybe in JSON format.
# JSON could be easily consumed by different kinds of client applications, whether it 
# would be a mobile app, a single page (SPA) browser app, a text based terminal app etc.  
print('Response from server:', response.text)
