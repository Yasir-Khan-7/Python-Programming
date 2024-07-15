#now here we are resampling the data
import pandas as pd
import time
# x = pd.read_csv('car_data.csv')

# print(x)
# index = pd.date_range(x, periods=9, freq='min')
# series = pd.Series(range(9), index=index)
# print(series)

# Sample data creation for demonstration
data = {
    'timestamp': pd.date_range(start='2023-01-01', periods=200, freq='T'),  # 200 rows of 1-minute intervals
    'speed': range(200),
    'distance': range(0, 400, 2)
}
df = pd.DataFrame(data)
print(df)
# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set the timestamp column as the index
df.set_index('timestamp', inplace=True)

# Resample the data to 5-minute intervals and calculate the mean for numeric columns
df_resampled = df.resample('5min').mean()

# Display the resampled data
print(df_resampled)
