import matplotlib.pyplot as plt
import pandas as pd

# Read in your CSV files using Pandas
df1 = pd.read_csv("solanafloor_DGOD_tokenFloor_2023-01-22-13-35.csv")
df2 = pd.read_csv("solanafloor_ABC_tokenFloor_2023-01-22-13-37.csv")

# Convert the DataFrame index to datetime format
df1.index = pd.to_datetime(df1['date'])
df2.index = pd.to_datetime(df2['date'])

# filter the dataframe to use only the values that are greater than or equal to the first date of the second dataframe
start_date = df2.index[0]
df1 = df1.loc[df1.index >= start_date]

# Create a line graph of the data
plt.plot(df1.index, df1['DeGods SOL'], color='blue', label='DeGods SOL')
plt.plot(df2.index, df2['ABC SOL'], color='red', label='ABC SOL')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Price Trends')

# Show legend and display the graph
plt.legend()
plt.show()
