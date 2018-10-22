import data_manager as dm
import data_models as models
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm
from sklearn.model_selection import train_test_split

'''
Just a code sninned having rolling correlations and OLS calculations.

'''


# Rolling correlations, "continuous correlation"

# rolling
# roll_df = models.ic_weather_roll_corr()

# print(roll_df.head(15))

# roll_df.plot.line(subplots=True)

# # data = [1,2,3,4,5]
# # df = pd.DataFrame(data)
# # print(df)
# # df.plot.bar()

# # plt.show()
# plt.savefig('timeseries_correlation') # no content!



# OLS 
# https://www.statsmodels.org/dev/examples/notebooks/generated/ols.html

# Consumption data y the one we wan't to predict
# X the weather data, the data that we think can explain or predict the consumption

# 1) pick electricity data source
#y = dm.get_industrial_electricity_data() # ic
y = dm.get_building_electricity_data()    # commercial mall, office etc.
# 2) weather data
X = dm.get_weather_data()

y = pd.DataFrame(y) # it's series so just convert to dataframe

# 3) join to dataframes to sync the datetime
joined_df = y.join(X)
joined_df = joined_df.dropna()


# 3b) subset of consumption data, 80%
data_80, test_data = train_test_split(joined_df, test_size=0.2, shuffle=False)

print(data_80.head())
print(data_80.tail())
print(data_80.shape)

# 4) Test and find the best combination of feattures (weather attributes) that explain the energy consumption

# 4a) divide to separate dataframes
y = pd.DataFrame(data_80['Demand/Usage'])

#X = data_80.drop(columns=['Demand/Usage'])  # all weather parameters
X = data_80.drop(columns=['Demand/Usage', 'U']) # drop humidity
#X = data_80.drop(columns=['Demand/Usage', 'T']) # drop temperature
#X = data_80.drop(columns=['Demand/Usage', 'T', 'Ff']) # drop temperature and wind speed
#X = data_80.drop(columns=['Demand/Usage', 'T', 'Ff', 'U']) # drop temperature, wind speed and humidity
#X = data_80.drop(columns=['Demand/Usage', 'T', 'Ff', 'U', 'P']) # drop temperature, wind speed, humidity and pressure
#X = data_80.drop(columns=['Demand/Usage', 'T', 'Ff', 'U', 'Td']) # drop temperature, wind speed, humidity and dewpoint temperature

# 4b) inititialize and run OLS model and print results
results = models.regression_model(y, X)

# model = sm.OLS(y, X)
# results = model.fit()
print(results.summary())