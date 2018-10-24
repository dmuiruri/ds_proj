#! /usr/bin/env python

"""This script contains models used to analyze the data."""


import pandas as pd
import data_manager as dm
import numpy as np
import statsmodels.api as sm
from scipy.stats import skew, kurtosis


def ic_weather_correlations():
    """
    Calculate static correlations.

    These are correlations between industrial electricity consumption and
    various weather parameters.
    """
    data = dm.get_ic_weather()
    return data.corr()


def ic_weather_roll_corr(win=12):
    """
    Calculate rolling correlations on hourly data.

    Rolling window is 12 hours
    """
    data = dm.get_ic_weather()
    ic_temp_corr = data['Demand/Usage'].rolling(win).corr(data['T'])
    ic_pres_corr = data['Demand/Usage'].rolling(win).corr(data['P'])
    ic_hum_corr = data['Demand/Usage'].rolling(win).corr(data['U'])
    ic_wind_corr = data['Demand/Usage'].rolling(win).corr(data['Ff'])
    ic_dewtemp_corr = data['Demand/Usage'].rolling(win).corr(data['Td'])
    corr_df = pd.DataFrame({'ic_T': ic_temp_corr, 'ic_P': ic_pres_corr,
                            'ic_U': ic_hum_corr, 'ic_Ff': ic_wind_corr,
                            'ic_dptemp': ic_dewtemp_corr})
    return corr_df.dropna()


def regression_model(Y, X):
    """Run a regression model."""
    model = sm.OLS(Y, X)
    results = model.fit()
    return results


def get_hourly_descriptive_stats():
    """
    Get descriptive statistics.

    Generates the descriptive statistics based on hourly data
    """
    weather = dm.get_weather_data()
    elec_cons = dm.get_all_elec_hourly_data()
    elec_price = pd.DataFrame(dm.get_price_data_hourly())
    data = elec_price.join(weather).join(elec_cons)  # amalgamated dataset
    data = data.sort_index().dropna()
    stats = [(item, np.mean(data[item]), np.min(data[item]),
             np.max(data[item]), np.std(data[item]), skew(data[item]),
             kurtosis(data[item])) for item in data.columns]
    stats_df = pd.DataFrame(stats, columns=['var', 'mean', 'min', 'max', 'std',
                            'skewness', 'kurtosis'])
    return stats_df


if __name__ == '__main__':
    """Add self tests."""

    print('Correlations between industrial Elec consumption and weather\n {}'.
          format(ic_weather_correlations()))
    print('Rolling correlations between elec consumption and weather\n {}'.
          format(ic_weather_roll_corr().head()))
    print('Run a regression model\n{}'.
          format(regression_model(dm.get_ic_weather()['Demand/Usage'],
                 dm.get_ic_weather()[['T', 'P', 'U', 'Ff', 'Td']]).summary()))
    print('Statistics\n{}\n'.format(get_hourly_descriptive_stats()))
