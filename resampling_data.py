import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('bms_data.csv')


# Convert Timestamp column to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Set the Timestamp column as the index
df.set_index('Timestamp', inplace=True)


# Resample the data to 5-minute intervals
resample_interval = '5T'
df_resampled = df.resample(resample_interval).mean()

# Plot the original and resampled data
plt.figure(figsize=(10, 6))

# Plot original data
plt.plot(df.index, df['CL_BMS_OPER_CODE[1]'], label='Original Data', alpha=0.5)

# Plot resampled data
plt.plot(df_resampled.index, df_resampled['CL_BMS_OPER_CODE[1]'], label=f'Resampled Data ({resample_interval} intervals)', color='red')

# Add labels, title, and legend
plt.xlabel('Time')
plt.ylabel('CL_BMS_OPER_CODE[1]')
plt.title('Original vs. Resampled Data')
plt.legend()
plt.show()
