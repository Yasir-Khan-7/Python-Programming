import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
fig, ax = plt.subplots(figsize=(10, 6))

# Initial empty plots for original and resampled data
original_line, = ax.plot([], [], label='Original Data', alpha=0.5)
resampled_line, = ax.plot([], [], label=f'Resampled Data ({resample_interval} intervals)', color='red')

# Add labels, title, and legend
ax.set_xlabel('Time')
ax.set_ylabel('CL_BMS_OPER_CODE[1]')
ax.set_title('Original vs. Resampled Data')
ax.legend()

# Update function for animation
def update(frame):
    # Select data up to the current frame
    current_time = df.index.min() + pd.Timedelta(seconds=frame)
    
    original_data = df[df.index <= current_time]
    resampled_data = df_resampled[df_resampled.index <= current_time]
    
    # Update the data of the plot lines
    original_line.set_data(original_data.index, original_data['CL_BMS_OPER_CODE[1]'])
    resampled_line.set_data(resampled_data.index, resampled_data['CL_BMS_OPER_CODE[1]'])
    
    # Adjust the x-axis limits
    ax.set_xlim(df.index.min(), df.index.max())
    
    # Adjust the y-axis limits dynamically
    y_min = min(original_data['CL_BMS_OPER_CODE[1]'].min(), resampled_data['CL_BMS_OPER_CODE[1]'].min())
    y_max = max(original_data['CL_BMS_OPER_CODE[1]'].max(), resampled_data['CL_BMS_OPER_CODE[1]'].max())
    ax.set_ylim(y_min, y_max)

    return original_line, resampled_line

# Total number of frames (seconds) for the animation
total_frames = int((df.index.max() - df.index.min()).total_seconds())

# Create the animation
ani = FuncAnimation(fig, update, frames=total_frames, blit=True, interval=50, repeat=False)

# Show the animation
plt.show()
