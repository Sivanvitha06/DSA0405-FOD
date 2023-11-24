import numpy as np

# Example values for time intervals and vertical positions
time_intervals = np.array([0, 1, 2, 3, 4])  # in seconds
vertical_positions = np.array([0, 5, 20, 45, 80])  # in meters

# Calculate the change in vertical position
change_in_position = np.diff(vertical_positions)

# Calculate the change in time
change_in_time = np.diff(time_intervals)

# Calculate the average velocity
average_velocity = change_in_position / change_in_time

# Print the results
print("Time Intervals:", time_intervals)
print("Vertical Positions:", vertical_positions)
print("Change in Vertical Position:", change_in_position)
print("Change in Time:", change_in_time)
print("Average Velocity:", average_velocity)

