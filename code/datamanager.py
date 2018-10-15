#! /usr/bin/env python

"""
This module provides access methods to datasets.

The files are stored locally and there could be some hardcoded paths
"""


import pandas as pd


def get_weather_data():
    """
    Pull weather data.

    Pulls data from the local directory and returns df of weather features
    """
    data = pd.io.parsers.read_csv('../weather.csv',
                                  index_col=0, parse_dates=True).sort_index()
    print('Weather Data Set\n{}'.format(data.head()))
    return data


def get_industrial_electricity_data():
    """
    Fetch industrial electricity consumption data.

    Returns a series of hourly consumption data in kWh.
    """
    data = pd.io.parsers.read_csv('../energy_industrial.csv',
                                  index_col=0, parse_dates=True)
    return data['Demand/Usage']
