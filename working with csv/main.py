# import csv
#
# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temp_list=[]
#     for row in data:
#         print(row)
#         if row[1]!='temp':
#             temp_list.append(row[1])
#
#     print(temp_list)

import pandas
import pandas as pd

data = pandas.read_csv("weather_data.csv")

# print(data)
# print (data["temp"].max())
# print(data["temp"].mean())
# print(data["temp"].mode())
#
# monday = data[data["day"]=="Monday"]
# print(monday)

max_temp = data[data["temp"]==data['temp'].max()]
print(max_temp)