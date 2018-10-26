
from flask_restful import Resource
from flask import request
import pandas as pd

'''
https://flask-restful.readthedocs.io/en/latest/api.html#flask_restful.Resource

'''


class HelloSpace(Resource):
    def get(self):
        '''
        Get a hello message
        ---
        responses:
          200:
            description: Message returned
        '''
        return {'message': 'Hello from space!'}


class PredictionModelIndustry(Resource):
      def get(self):
        '''
        Get the energy consumption prediction for insdusty
        ---
        responses:
          200:
            description: The prediction data in JSON format
        '''

      





        return {'message': "This will be the IC prediction JSON"} 