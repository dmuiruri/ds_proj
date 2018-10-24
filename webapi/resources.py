
from flask_restful import Resource
from flask import request
import pandas as pd

'''
https://flask-restful.readthedocs.io/en/latest/api.html#flask_restful.Resource

'''


class HelloSpace(Resource):
    def get(self):
        # swagger_from_file: /hello.yml

        '''
        Get a hello message
        ---
        responses:
          200:
            description: Message returned
        '''
        return {'message': 'Hello from space to space!'}


class PredictionModel(Resource):
    def get(self):
        # swagger_from_file: /prediction.yml
        # 
        '''
        Just ping
        ---
        responses:
          200:
            description: Ok message
        '''
        return {'message': "I'm alive!"} 

    def post(self):       
        '''
        Get a prediction/forecast of energy consumption based on consumption data and weather data
        ---
        parameters:
          - in: body
        responses:
          200:
            description: Prediction result(s)
          400:
            description: Request was broken (propably the request payload)
        '''
        # https://stackoverflow.com/questions/11817182/uploading-multiple-files-with-flask
        forecast_base_data = request.files.getlist("files")

        # first file is energy consumption the second is weather
        consumption_csv = forecast_base_data[0]
        weather_csv = forecast_base_data[1]

        # init dataframes
        c_data = pd.io.parsers.read_csv(consumption_csv)
        w_data = pd.io.parsers.read_csv(weather_csv)
        print(c_data.head())
        print(w_data.head())


        # TODO: call the model


        return {'message': 'Here will be a electricity consumption forecast. '}   