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
    data = pd.io.parsers.read_csv('../data/hourly_resampled_weather_data.csv',
                                  index_col=0, parse_dates=True).sort_index()
    return data


def get_industrial_electricity_data():
    """
    Fetch industrial electricity consumption data.

    Returns a series of hourly consumption data in kWh.
    """
    data = pd.io.parsers.read_csv('../data/energy_industrial.csv',
                                  index_col=0, parse_dates=True)
    return data['Demand/Usage']
    

def get_building_electricity_data():
    """
    Fetch building electricity consumption data.

    Returns a series of hourly consumption data in kWh.
    """
    data = pd.io.parsers.read_csv('../data/energy_building.csv',
                                  index_col=0, parse_dates=True)
    return data['Demand/Usage']    


def get_ic_weather():
    """
    Get industrial electricity consumption and weather dataself.

    Returns the two datasets as one dataframe
    """
    data = pd.io.parsers.read_csv('../data/weather_elec_data.csv',
                                  index_col=0, parse_dates=True)
    return data


if __name__ == '__main__':
    print('Weather data\n {} \n'.format(
            get_weather_data().head()))
    print('Industrial Electricity Consumtion Data\n{}\n'.format(
            get_industrial_electricity_data().head()))
    print('Weather and Industrial electricity consumption\n{}\n'.format(
            get_ic_weather().head()))
