#! /usr/bin/env python

"""
This module provides access methods to datasets.

The files are stored locally and there could be some hardcoded paths
"""


import pandas as pd
import os


# csv file location in local dev env
DATA_FILE_PATH = '../data/'

is_heroku = os.environ.get('CURRENT_ENV', None)
    
if is_heroku:
    # csv file location in heroku
    DATA_FILE_PATH = '/app/data/'


def get_weather_data():
    """
    Pull weather data.

    Pulls data from the local directory and returns df of weather features
    """
    data = pd.io.parsers.read_csv(DATA_FILE_PATH + 'hourly_resampled_weather_data.csv',
                                  index_col=0, parse_dates=True).sort_index()
    return data


def get_industrial_electricity_data():
    """
    Fetch industrial electricity consumption data.

    Returns a series of hourly consumption data in kWh.
    """
    data = pd.io.parsers.read_csv(DATA_FILE_PATH + 'energy_industrial.csv',
                                  index_col=0, parse_dates=True)
    return data['Demand/Usage']


def get_building_electricity_data():
    """
    Fetch building electricity consumption data.

    Returns a series of hourly consumption data in kWh.
    """
    data = pd.io.parsers.read_csv(DATA_FILE_PATH + 'energy_building.csv',
                                  index_col=0, parse_dates=True)
    return data['Demand/Usage']


def get_cre_electricity_data():
    """
    Fetch cre electricity consumption data.

    Returns a series of hourly consumption data in kWh.
    """
    data = pd.io.parsers.read_csv(DATA_FILE_PATH + 'cre_total.csv',
                                  index_col=0, parse_dates=True)
    return data['Demand/Usage']


def get_all_elec_hourly_data():
    """
    Get hourly data.

    Get all data in hourly format
    """
    industry = get_industrial_electricity_data()
    building = get_building_electricity_data()
    cre = get_cre_electricity_data()
    return pd.DataFrame({'industry': industry, 'building': building,
                        'cre': cre})


def get_ic_weather():
    """
    Get industrial electricity consumption and weather dataself.

    Returns the two datasets as one dataframe
    """
    data = pd.io.parsers.read_csv(DATA_FILE_PATH + 'weather_elec_data.csv',
                                  index_col=0, parse_dates=True)
    return data


def get_csv_data(path, parseDates=True, indexCol=None):
    """
    Get data using a generic path string.

    Helper function to fetch arbitrary files in the repo.
    """
    return pd.io.parsers.read_csv(path,
                                  parse_dates=parseDates, index_col=indexCol)


def get_price_data_hourly():
    """
    Get electricity price data.

    Data is based on exchange prices
    """
    data = pd.io.parsers.read_csv(DATA_FILE_PATH + 'price_data_italy_fixed.csv')
    data.set_index('DateTime', inplace=True)
    return data['PUN']


if __name__ == '__main__':
    """Test"""
    print('Weather data\n {} \n'.format(
            get_weather_data().head()))
    print('Industrial Electricity Consumtion Data\n{}\n'.format(
            get_industrial_electricity_data().head()))
    print('Building Electricity Consumtion Data\n{}\n'.format(
            get_building_electricity_data().head()))
    print('CRE Electricity Consumtion Data\n{}\n'.format(
            get_cre_electricity_data().head()))
    print('Weather and Industrial electricity consumption\n{}\n'.format(
            get_ic_weather().head()))
    print('Get generic data from the repository\n{}\n'.format(
            get_csv_data('../data/energy_building.csv', indexCol=0).head()))
    print('Get all consumption data in hourly format\n{}\n'.
          format(get_all_elec_hourly_data().head()))
    print('Get Price data\n{}\n'.format(get_price_data_hourly().head()))
