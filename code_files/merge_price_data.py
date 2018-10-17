## PLOTS
# weather data weekly and daily in two sub plots

import matplotlib.pyplot as plt
import pandas as pd


# merge date and hour columns in price data

price_data = pd.read_csv('../price_data_italy.csv')

# drop the extra 25 hour
price_data = price_data[(price_data.HOUR != 25)]

price_data['Time'] = price_data['HOUR'].apply(lambda x: '00:00' if (x == 24) else (str(x) + ':00')) # apply(lambda x: str(x) + ':00')
price_data["DateTime"] = price_data["Date"].map(str) + ' ' + price_data["Time"].apply(lambda x: ('0' + x) if (len(x) == 4) else x)

price_data = price_data.drop(columns=['Time', 'HOUR', 'Date'])


price_data['DateTime'] = pd.to_datetime(price_data["DateTime"], format='%Y-%m-%d %H:%M', utc=True)

price_data.to_csv('../data/price_data_italy_fixed.csv')
#print(price_data.head())




