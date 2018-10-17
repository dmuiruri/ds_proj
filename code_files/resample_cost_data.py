import pandas as pd
from datetime import datetime
import numpy as np


hourly_cost_data = pd.read_csv('../data/ic_cost.csv')

print(hourly_cost_data.head())

# explicitly convert the date
hourly_cost_data['DateTime'] = pd.to_datetime(hourly_cost_data['DateTime'], format='%Y-%m-%d %H:%M', utc=True)

# set the DateTime column as the new index for the hourly_cost_data
hourly_cost_data = hourly_cost_data.set_index('DateTime')

# sample daily and sum the costs
daily_cost_data = hourly_cost_data.resample('D').sum()
print(daily_cost_data.head())

# sample monthly and sum the costs
monthly_cost_data = daily_cost_data.resample('M').sum()
#print(monthly_cost_data)
#print(monthly_cost_data.iloc[1:12])
#print(monthly_cost_data.iloc[1:12].mean())

monthly_cost_data.to_csv('../data/monthly_cost_data.csv')



