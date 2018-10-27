
from flask_restful import Resource, reqparse
from flask import request
import pandas as pd
import src.data_models as dm
import json

'''

This file specifies the HTTP API endpoints (resources) for the electricity 
consumption prediction service.


About Flask and flask-restful see:
https://flask-restful.readthedocs.io/en/latest/api.html#flask_restful.Resource

About Swagger and API documentation see:
https://github.com/gangverk/flask-swagger

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
        Get the energy consumption prediction for industry
        ---
        parameters:
          - in: query
            name: sampling
            description: Specifies the sampling interval for returned prediction data. Default sampling interval/rate is hourly if none given. Other possible values are daily, weekly and monthly.
            type: string
        responses:
          200:
            description: The prediction data in JSON format
        '''
        sample_interval = None

        parser = reqparse.RequestParser()
        parser.add_argument('sampling', type=str)
        args = parser.parse_args(strict=True) # no other args allowed than sampling

        print('re:', args.items())

        # this is hourly sampled data
        df = dm.predict_industry_elec_cons()
                   
        if sample_interval is None:
            print('Using default hourly sampling interval.')
            return df.to_json()
        elif sample_interval == 'daily':
            print('Daily sampling interval requested.')
            # TODO resample and return
        elif sample_interval == 'weekly':
            print('weekly sampling interval requested.')
            # TODO resample and return
        elif sample_interval == 'monthly':
            print('Monthly sampling interval requested.')
            # TODO resample and return
        else:
            raise ValueError('Unknown sampling interval was requested: ', sample_interval)


class PredictionModelBuilding(Resource):
    def get(self):
        '''
        Get the energy consumption prediction for building
        ---
        parameters:
          - in: query
            name: sampling
            description: Specifies the sampling interval for returned prediction data. Default sampling interval/rate is hourly if none given. Other possible values are daily, weekly and monthly.
            type: string
        responses:
          200:
            description: The prediction data in JSON format
        '''
        
        return {"message": "Building prediction TBD"}


class PredictionModelConsumer(Resource):
    def get(self):
        '''
        Get the energy consumption prediction for consumer
        ---
        parameters:
          - in: query
            name: sampling
            description: Specifies the sampling interval for returned prediction data. Default sampling interval/rate is hourly if none given. Other possible values are daily, weekly and monthly.
            type: string
        responses:
          200:
            description: The prediction data in JSON format
        '''
        
        return {"message": "Consumer prediction TBD"}