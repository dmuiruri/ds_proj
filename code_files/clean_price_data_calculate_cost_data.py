import matplotlib.pyplot as plt
import pandas as pd
import data_manager as dm


'''
    Clean the price data by merging date and hour columns into new DateTime column

'''

price_data = pd.read_csv('../price_data_italy.csv')

# drop the extra 25 hour
price_data = price_data[(price_data.HOUR != 25)]

# construct the DateTime column
price_data['Time'] = price_data['HOUR'].apply(lambda x: '00:00' if (x == 24) else (str(x) + ':00'))
price_data["DateTime"] = price_data["Date"].map(str) + ' ' + price_data["Time"].apply(lambda x: ('0' + x) if (len(x) == 4) else x)

# remove extra columns
price_data = price_data.drop(columns=['Time', 'HOUR', 'Date'])

price_data['DateTime'] = pd.to_datetime(price_data["DateTime"], format='%Y-%m-%d %H:%M', utc=True)

price_data.to_csv('../data/price_data_italy_fixed.csv')



'''
    Calculate cost based on consumption and price (consumption in megawatts)

'''
# price data
price_data = pd.read_csv('../data/price_data_italy_fixed.csv')
price_data = price_data.set_index('DateTime')

# consumption data 
ic_df = dm.get_industrial_electricity_data() # till 11AM 18.5.2018

# to mega watts
demand_in_mw = ic_df / 1000   # till 00:00 18.5.2018

ic_cost = price_data['PUN'] * demand_in_mw
ic_cost = ic_cost.dropna()

cost_dataframe = pd.DataFrame(data=ic_cost, columns=['cost'])

#print(cost_dataframe.head())
#print(cost_dataframe.shape)

cost_dataframe.to_csv('../data/ic_cost.csv')