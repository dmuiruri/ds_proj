#! /usr/bin/env python
"""Module contains graphing code."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import matplotlib.dates as mdates

import data_manager as dm


def create_elec_demand_plot():
    """
    Create plot.

    Generates a plot with Monthly data
    """
    fig = plt.figure()  # subplot(3, 1, sharex='col')
    fig.set_size_inches(6, 3.375)

    # Create the sub-plots
    print('Creating subplots...')
    industry_plot = plt.subplot(311)
    building_plot = plt.subplot(312)
    cre_plot = plt.subplot(313)

    print('Fetching data...')
    df = dm.get_all_elec_hourly_data()
    industrial = df['industry']
    building = df['building']
    cre = df['cre']

    # Resample to monthly consumption
    industrial_m = industrial.resample('M').sum()
    building_m = building.resample('M').sum()
    cre_m = cre.resample('M').sum()

    print('Plot the data...')
    industry_plot.bar(np.arange(len(building_m)), industrial_m, width=0.5,
                      color='#ff6f59', label='Industrial')
    industry_plot.spines['top'].set_visible(False)
    industry_plot.spines['right'].set_visible(False)
    plt.setp(industry_plot.get_xticklabels(), visible=False)
    industry_plot.legend(loc=1, prop={'size': 6})

    building_plot.bar(np.arange(len(building_m)), building_m, width=0.5,
                      color='#254441', label='Commercial Building')
    building_plot.spines['top'].set_visible(False)
    building_plot.spines['right'].set_visible(False)
    plt.setp(building_plot.get_xticklabels(), visible=False)
    building_plot.legend(loc=1, prop={'size': 6})

    cre_plot.bar(np.arange(len(building_m)), cre_m, width=0.5, color='#43aa8b',
                 label='Residential')
    cre_plot.spines['top'].set_visible(False)
    cre_plot.spines['right'].set_visible(False)
    cre_plot.legend(loc=1, prop={'size': 6})
    cre_plot.set_xticklabels(('Apr-17', 'May-17', 'Jul-/17', 'Sep-17',
                             'Nov-17', 'Jan-18', 'Mar-18', 'May-18'))

    print('Save the plot to local disk...')
    fig.tight_layout()
    fig.savefig('../docs/assets/images/monthly_elec_demand.png', frameon=False)
    print('Plot complete and file saved...')


def create_weather_plot():
    """
    Create weather data summary.

    Plot the data based on monthly summary
    """
    fig = plt.figure()  # subplot(3, 1, sharex='col')
    fig.set_size_inches(6, 3.375)

    # Create the sub-plots
    print('Creating subplots...')
    T_plot = plt.subplot(511)
    U_plot = plt.subplot(512)
    FF_plot = plt.subplot(513)
    P_plot = plt.subplot(514)
    TD_plot = plt.subplot(515)

    print('Fetching data...')
    df = dm.get_weather_data()
    T = df['T']
    U = df['U']
    FF = df['Ff']
    P = df['P']
    TD = df['Td']

    # Resample to monthly consumption
    T_m = T.resample('M').mean()
    U_m = U.resample('M').mean()
    FF_m = FF.resample('M').mean()
    P_m = P.resample('M').mean()
    TD_m = TD.resample('M').mean()

    print('Plot the data...')
    T_plot.bar(np.arange(len(T_m)), T_m, width=0.5, color='#ff6f59',
               label='Temp')
    T_plot.spines['top'].set_visible(False)
    T_plot.spines['right'].set_visible(False)
    plt.setp(T_plot.get_xticklabels(), visible=False)
    T_plot.legend(loc=1, prop={'size': 6})

    U_plot.bar(np.arange(len(U_m)), U_m, width=0.5, color='#254441',
               label='Humidity')
    U_plot.spines['top'].set_visible(False)
    U_plot.spines['right'].set_visible(False)
    plt.setp(U_plot.get_xticklabels(), visible=False)
    U_plot.legend(loc=1, prop={'size': 6})

    FF_plot.bar(np.arange(len(FF_m)), FF_m, width=0.5, color='#43aa8b',
                label='Wind Speed')
    FF_plot.spines['top'].set_visible(False)
    FF_plot.spines['right'].set_visible(False)
    plt.setp(FF_plot.get_xticklabels(), visible=False)
    FF_plot.legend(loc=1, prop={'size': 6})

    P_plot.bar(np.arange(len(P_m)), P_m, width=0.5, color='#b2b09b',
               label='Pressure')
    P_plot.spines['top'].set_visible(False)
    P_plot.spines['right'].set_visible(False)
    plt.setp(P_plot.get_xticklabels(), visible=False)
    P_plot.legend(loc=1, prop={'size': 6})

    TD_plot.bar(np.arange(len(TD_m)), TD_m, width=0.5, color='#ef3054',
                label='Dew Point Temp')
    TD_plot.spines['top'].set_visible(False)
    TD_plot.spines['right'].set_visible(False)
    TD_plot.set_xticklabels(('Apr-17', 'May-17', 'Jul-17', 'Sep-17', 'Nov-17',
                            'Jan-18', 'Mar-18', 'May-18'))
    TD_plot.legend(loc=1, prop={'size': 6})

    print('Save the plot to local disk...')
    fig.tight_layout()
    fig.savefig('../docs/assets/images/monthly_weather.png', frameon=False)
    print('Plot complete and file saved...')


def create_elec_price_plot():
    """
    Create plot.

    Generates a plot with Monthly data
    """
    fig = plt.figure()  # subplot(3, 1, sharex='col')
    fig.set_size_inches(6, 3.375)

    # Create the sub-plots
    print('Creating plot...')
    price_plot = plt.subplot()

    print('Fetching data...')
    price = dm.get_price_data_hourly()
    price.index = pd.to_datetime(price.index)

    # Resample to monthly consumption
    price_m = price.resample('M').mean()

    print('Plot the data...')
    price_plot.bar(np.arange(len(price_m)), price_m, width=0.5,
                   color='#ff6f59', label='Average Price (€/MWh)')
    price_plot.spines['top'].set_visible(False)
    price_plot.spines['right'].set_visible(False)
    # plt.setp(price_plot.get_xticklabels(), visible=False)
    price_plot.legend(loc=1, prop={'size': 6})
    price_plot.set_xticklabels(('Apr-17', 'May-17', 'Jul-/17', 'Sep-17',
                               'Nov-17', 'Jan-18', 'Mar-18', 'May-18'))

    print('Save the plot to local disk...')
    fig.tight_layout()
    fig.savefig('../docs/assets/images/monthly_elec_price.png', frameon=False)
    print('Plot complete and file saved...')


if __name__ == '__main__':
    """Test"""
    create_elec_demand_plot()
    create_weather_plot()
    create_elec_price_plot()
