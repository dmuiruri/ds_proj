
from flask_restful import Resource, reqparse, abort
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

def sampling_interval_from_request():
    '''
    Parse and return the value of the sampling parameter from client Request

    '''
    parser = reqparse.RequestParser()
    parser.add_argument('sampling', type=str)
    args = parser.parse_args(strict=True) # no other args allowed than sampling
    return args.sampling


def resample_hourly_to_daily(df):
    df = df.resample('D').sum()
    print('Daily data: ', df.head())
    return df


def resample_hourly_to_weekly(df):
    df = df.resample('D').sum().resample('W').sum()
    print('Weekly data: ', df.head())
    return df


def resample_hourly_to_monthly(df):
    df = df.resample('D').sum().resample('W').sum().resample('M').sum()
    print('Monthly data: ', df.head())
    return df



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
        Energy consumption prediction for industrial building.
        ---
        parameters:
          - in: query
            name: sampling
            description: Specifies the sampling interval for returned prediction data. Default sampling interval/rate is hourly if none given. Other possible values are daily, weekly and monthly.
            type: string
        responses:
          200:
            description: The prediction data in JSON format.
          400:
            description: Error if unknown sampling interval was requested.
        '''
        sampling_interval = None
        sampling_interval = sampling_interval_from_request()

        # this is hourly sampled data
        df = dm.predict_industry_elec_cons()

        if sampling_interval is None:
            print('Using default hourly sampling interval.')
            return df.to_json()
        elif sampling_interval == 'daily':
            print('Daily sampling interval requested.')
            return resample_hourly_to_daily(df).to_json()
        elif sampling_interval == 'weekly':
            print('weekly sampling interval requested.')
            return resample_hourly_to_weekly(df).to_json()
        elif sampling_interval == 'monthly':
            print('Monthly sampling interval requested.')
            return resample_hourly_to_monthly(df).to_json()
        else:
           abort(400, error_message='Unknown sampling interval was requested: ' + sampling_interval)


class PredictionModelCommercialBuilding(Resource):
    def get(self):
        '''
        Energy consumption prediction for a commercial building.
        ---
        parameters:
          - in: query
            name: sampling
            description: Specifies the sampling interval for returned prediction data. Default sampling interval/rate is hourly if none given. Other possible values are daily, weekly and monthly.
            type: string
        responses:
          200:
            description: The prediction data in JSON format
          400:
            description: Error if unknown sampling interval was requested.
        '''
        sampling_interval = None
        sampling_interval = sampling_interval_from_request()

        # this is hourly sampled data for consumer building
        df = dm.predict_blg_elec_cons()

        if sampling_interval is None:
            print('Using default hourly sampling interval.')
            return df.to_json()
        elif sampling_interval == 'daily':
            print('Daily sampling interval requested.')
            return resample_hourly_to_daily(df).to_json()
        elif sampling_interval == 'weekly':
            print('weekly sampling interval requested.')
            return resample_hourly_to_weekly(df).to_json()
        elif sampling_interval == 'monthly':
            print('Monthly sampling interval requested.')
            return resample_hourly_to_monthly(df).to_json()
        else:
           abort(400, error_message='Unknown sampling interval was requested: ' + sampling_interval)


class PredictionModelApartmentBuilding(Resource):
    def get(self):
        '''
        Energy consumption prediction for an apartment building.
        ---
        parameters:
          - in: query
            name: sampling
            description: Specifies the sampling interval for returned prediction data. Default sampling interval/rate is hourly if none given. Other possible values are daily, weekly and monthly.
            type: string
        responses:
          200:
            description: The prediction data in JSON format
          400:
            description: Error if unknown sampling interval was requested.
        '''
        sampling_interval = None
        sampling_interval = sampling_interval_from_request()

        # this is hourly sampled data for consumer building
        df = dm.predict_apt_elec_cons()

        if sampling_interval is None:
            print('Using default hourly sampling interval.')
            return df.to_json()
        elif sampling_interval == 'daily':
            print('Daily sampling interval requested.')
            return resample_hourly_to_daily(df).to_json()
        elif sampling_interval == 'weekly':
            print('weekly sampling interval requested.')
            return resample_hourly_to_weekly(df).to_json()
        elif sampling_interval == 'monthly':
            print('Monthly sampling interval requested.')
            return resample_hourly_to_monthly(df).to_json()
        else:
           abort(400, error_message='Unknown sampling interval was requested: ' + sampling_interval)