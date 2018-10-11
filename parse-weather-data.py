
import pandas as pd
import numpy as np
import csv

# parse weather csv to same form as electricity data
# 00:50 --> 01:00
# 01:20 01:50 --> 02:00 (count average of two temps)
# drop other clumns than data time and temperature


# read csv 
weather_data_frame = pd.read_csv('weather-Rome_mod.csv')


print('hello')

# Advance hour by one and reset the minutes
# 23:xx -> 00:00
# 22:xx -> 23:00
# 21:xx -> 22:00
#   ...
# 00:xx -> 01:00
def round_the_clock(date_time_str):
    new_time_str = ''
    # 18.05.2018 22:20
    if date_time_str[-5:-3] == '23':
        new_time_str = date_time_str[:11] + '00:00'
    else:
        new_hour = int(float(date_time_str[-5:-3])) + 1
        new_time_str = date_time_str[:11] + str(new_hour) + ':00'
    #print('new time new time: ', new_time_str)
    return new_time_str


def write_to_new_csv(dataframe): 
    with open('weather_data_final.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)                     
        filewriter.writerow(['DateTime', 'T', 'P', 'U', 'Ff', 'Td'])    

        buffer_row_arr = []
        for index, row in dataframe.iterrows():
            #filewriter.writerow(dataframe.iat[index,0].split(';'))
            #print(row)
            row_value_array = row[0].split(';')
            
            if row_value_array[0][-2:] == '50':
                buffer_row_arr = row_value_array
            else:
                if len(buffer_row_arr) == 0:
                    # just write
                    filewriter.writerow(row_value_array)
                else:
                    average_arr = []

                    # Calculate averages
                    average_arr.append(round_the_clock(row_value_array[0])) 
                    average_arr.append((float(row_value_array[1]) + float(buffer_row_arr[1]))/2) # temperature
                    average_arr.append((float(row_value_array[2]) + float(buffer_row_arr[2]))/2) # P
                    average_arr.append((float(row_value_array[3]) + float(buffer_row_arr[3]))/2) # U
                    average_arr.append((float(row_value_array[4]) + float(buffer_row_arr[4]))/2) # Ff
                    average_arr.append((float(row_value_array[5]) + float(buffer_row_arr[5]))/2) # Td

                    filewriter.writerow(average_arr)
                    buffer_row_arr = []

        
        
sub_data_frame = weather_data_frame.head(47) # one day
print(sub_data_frame)
write_to_new_csv(sub_data_frame)

#write_to_new_csv(weather_data_frame)
