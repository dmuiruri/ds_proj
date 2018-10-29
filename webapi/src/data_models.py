#! /usr/bin/env python

"""This script contains models used to analyze the data."""


import pandas as pd
import src.data_manager as dm
import numpy as np
import statsmodels.api as sm
from scipy.stats import skew, kurtosis
from sklearn.model_selection import train_test_split


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


def run_industry_regression():
    """
    Run a regression model for the industry dataset.

    This regression model estimates the parameters using the entire dataset.
    """
    weather = dm.get_weather_data()
    elec_cons = dm.get_all_elec_hourly_data()
    data = elec_cons.join(weather)  # amalgamated dataset
    data = data.sort_index().dropna()

    Y = data['industry']
    X = data[['P', 'U', 'Ff', 'Td']]
    res = regression_model(Y, X)
    return res


def predict_industry_elec_cons():
    """
    Predict electricity consumption for an industrial consumer.

    This function returns predicted values for four weeks (one month)
    """
    weather = dm.get_weather_data()
    elec_cons = dm.get_all_elec_hourly_data()
    data = elec_cons.join(weather)  # amalgamated dataset
    data = data.sort_index().dropna()

    train, test = train_test_split(data, train_size=0.85, shuffle=False)
    print('Test data is {:2.2%} of the data\n'.
          format(len(train), len(test), len(test)/len(data)))
    # print('Train data head\n{}\n {}\n'.format(train.head(), train.tail()))
    # print('Test data head\n{}\n {}\n'.format(test.head(), test.tail()))
    Y = train['industry']
    X = train[['P', 'U', 'Ff', 'Td']]
    res = sm.OLS(Y, X).fit()
    predictions = res.predict(test[['P', 'U', 'Ff', 'Td']])
    # print('Predictions are {}\n {}\n {}\n'.format(
    #       predictions.head(), predictions.head(), predictions.tail()))
    return pd.DataFrame({'y^': predictions, 'y': test['industry'],
                        'diff': predictions - test['industry']})


def predict_blg_elec_cons():
    """
    Predict electricity consumption for an commercial building.

    This function returns predicted values for four weeks (one month)
    """
    weather = dm.get_weather_data()
    elec_cons = dm.get_all_elec_hourly_data()
    data = elec_cons.join(weather)  # amalgamated dataset
    data = data.sort_index().dropna()

    train, test = train_test_split(data, train_size=0.85, shuffle=False)
    print('Test data is {:2.2%} of the data\n'.
          format(len(train), len(test), len(test)/len(data)))
    # print('Train data head\n{}\n {}\n'.format(train.head(), train.tail()))
    # print('Test data head\n{}\n {}\n'.format(test.head(), test.tail()))
    Y = train['building']
    X = train[['P', 'U', 'Ff', 'Td']]
    res = sm.OLS(Y, X).fit()
    predictions = res.predict(test[['P', 'U', 'Ff', 'Td']])
    # print('Predictions are {}\n {}\n {}\n'.format(
    #       predictions.head(), predictions.head(), predictions.tail()))
    return pd.DataFrame({'y^': predictions, 'y': test['building'],
                        'diff': predictions - test['building']})


def predict_apt_elec_cons():
    """
    Predict electricity consumption for an apartment building.

    This function returns predicted values for four weeks (one month)
    """
    weather = dm.get_weather_data()
    elec_cons = dm.get_all_elec_hourly_data()
    data = elec_cons.join(weather)  # amalgamated dataset
    data = data.sort_index().dropna()

    train, test = train_test_split(data, train_size=0.85, shuffle=False)
    print('Test data is {:2.2%} of the data\n'.
          format(len(train), len(test), len(test)/len(data)))
    # print('Train data head\n{}\n {}\n'.format(train.head(), train.tail()))
    # print('Test data head\n{}\n {}\n'.format(test.head(), test.tail()))
    Y = train['cre']
    X = train[['P', 'U', 'Ff', 'Td']]
    res = sm.OLS(Y, X).fit()
    predictions = res.predict(test[['P', 'U', 'Ff', 'Td']])
    # print('Predictions are {}\n {}\n {}\n'.format(
    #       predictions.head(), predictions.head(), predictions.tail()))
    return pd.DataFrame({'y^': predictions, 'y': test['cre'],
                        'diff': predictions - test['cre']})


if __name__ == '__main__':
    """Add self tests."""

    # print('Correlations between industrial Elec consumption and weather\n {}'.
    #       format(ic_weather_correlations()))
    # print('Rolling correlations between elec consumption and weather\n {}'.
    #       format(ic_weather_roll_corr().head()))
    # print('Run a regression model\n{}'.
    #       format(regression_model(dm.get_ic_weather()['Demand/Usage'],
    #              dm.get_ic_weather()[['T', 'P', 'U', 'Ff', 'Td']]).summary()))
    # print('Statistics\n{}\n'.format(get_hourly_descriptive_stats()))
    print('Industry regression \n{}\n'.format(run_industry_regression()))
