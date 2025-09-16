import pandas as pd
#Task 1
# Read a dataset
destination = pd.read_csv("C:/Users/HP/OneDrive/Desktop/Ty  - Fall 2023/Programming/Wk2/Datasets/flights.csv")

#show the number of rows and columns that exist
num_row, number_column = destination.shape
print(f"Number of row: {num_row}")
print(f"Number of column: {number_column}")

#show the dtypes
row_dtypes = destination.dtypes
print(row_dtypes)

# show the number of carriers that exist
carrier_number = destination["carrier"].nunique()
print(f"Number of carriers: {carrier_number}")

# size of carrier in terms of the number of flight
carrier_size = destination.groupby("carrier")[["flight"]].count()
print(carrier_size)

#show the mean dep_delay and arr_delay for each flight
carrier_flight = destination.groupby("flight")[["dep_delay", "arr_delay"]].mean()
dep_carrier_flight = carrier_flight.sort_values(by="dep_delay", ascending=False)
arr_carrier_flight = carrier_flight.sort_values(by="arr_delay", ascending=False)
print(dep_carrier_flight)
print(arr_carrier_flight)

#Task 2 - 2
data_winter = destination[destination['month'].isin([1, 2])]
#filter data for summer
data_summer = destination[destination['month'].isin([6, 7])]
#calculate the average
average_winter = data_winter['arr_delay'].mean()
average_summer = data_summer['arr_delay'].mean()
#comparing results
if average_winter > average_summer:
   print("more delays happen in winter")
elif average_winter < average_summer:
   print("more delays happen in summer")
else:
   print("delays are similar")

