
import pandas as pd
import numpy as np
import csv

'''
  parse weather csv to same form as electricity data
  00:50 --> 01:00
  01:20 + 01:50 --> 02:00 (count average of the values)
  drop other columns than 'DateTime', 'T', 'P', 'U', 'Ff' and 'Td'
'''

# the destination file created from from the source data
OUTPUT_CSV_FILE = 'weather_data_final.csv'
# the source data file
INPUT_CSV_FILE = 'weather-Rome_mod.csv'

# read the "raw" source data 
weather_data_frame = pd.read_csv(INPUT_CSV_FILE)


def round_the_clock(date_time_str):
    '''
    Advance hour by one and reset the minutes
        23:xx -> 00:00
        22:xx -> 23:00
        21:xx -> 22:00
        ...
        00:xx -> 01:00
     '''
    new_time_str = ''
    # 18.05.2018 22:20
    if date_time_str[-5:-3] == '23':
        new_time_str = date_time_str[:11] + '24:00'
    else:
        new_hour = str(int(float(date_time_str[-5:-3])) + 1)
        if len(new_hour) == 1:
            new_hour = '0' + new_hour
        new_time_str = date_time_str[:11] + new_hour + ':00'
    #print('new time new time: ', new_time_str)
    return new_time_str


def check_empty_data_values(row_value_array):
    '''
        Check the data for empty values. 
        All our values (except the datetime) are numerical so now just 
        populating possible empty values with 0.
    '''
    if row_value_array[0] == '':
        raise ValueError('Date not found from the source data!', row_value_array)
    if row_value_array[1] == '':
        row_value_array[1] = 0
        print('T was empty in source data.', row_value_array)
    if row_value_array[2] == '':
        row_value_array[2] = 0
        print('P was empty in source data.', row_value_array)
    if row_value_array[3] == '':
        row_value_array[3] = 0
        print('U was empty in source data.', row_value_array)
    if row_value_array[4] == '':
        row_value_array[4] = 0
        print('Ff empty in source data.', row_value_array)
    if row_value_array[5] == '':
        row_value_array[5] = 0
        print('Td empty in source data.', row_value_array)

    # TODO: Is this ok?
    return row_value_array


def write_to_new_csv(dataframe): 
    '''
        Create new csv file from the given dataframe.
        The source data contains two weather entries per hour, merge these two
        into a one row by counting averages for the values and resetting the time.
    '''

    with open(OUTPUT_CSV_FILE, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        filewriter.writerow(['DateTime', 'T', 'P', 'U', 'Ff', 'Td'])    

        buffer_row_arr = []
        for index, row in dataframe.iterrows():

            row_value_array = check_empty_data_values(row[0].split(';'))
            
            if row_value_array[0][-2:] == '50':
                buffer_row_arr = row_value_array
            else:
                if len(buffer_row_arr) == 0:
                    # just write
                    filewriter.writerow(row_value_array)
                else:
                    average_arr = []

                    # Calculate averages
                    try:
                        average_arr.append(round_the_clock(row_value_array[0])) 
                        average_arr.append((float(row_value_array[1]) + float(buffer_row_arr[1]))/2) # temperature
                        average_arr.append((float(row_value_array[2]) + float(buffer_row_arr[2]))/2) # P
                        average_arr.append((float(row_value_array[3]) + float(buffer_row_arr[3]))/2) # U
                        average_arr.append((float(row_value_array[4]) + float(buffer_row_arr[4]))/2) # Ff
                        average_arr.append((float(row_value_array[5]) + float(buffer_row_arr[5]))/2) # Td
                    except ValueError as error:
                        print('ValueError: ', error)
                        print(' Current row_value_array ', row_value_array)
                        print(' Current buffer_row_arr ', buffer_row_arr)

                    filewriter.writerow(average_arr)
                    buffer_row_arr = []

        
        
#sub_data_frame = weather_data_frame.head(100 * 47) # n days
#print(sub_data_frame)
#write_to_new_csv(sub_data_frame)

write_to_new_csv(weather_data_frame)


# some stats for sanity check
weather_data = pd.read_csv(OUTPUT_CSV_FILE)
print('Columns: ', weather_data.columns.tolist())
print(weather_data.describe())

