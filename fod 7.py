import numpy as np

# Assuming 'house_data' is a NumPy array with columns like [bedrooms, square_footage, sale_price]
# Load your dataset into 'house_data' accordingly

# Example data (replace this with your actual data)
house_data = np.array([
    [3, 1500, 200000],
    [4, 1800, 250000],
    [5, 2000, 300000],
    [4, 1600, 220000],
    [3, 1400, 190000]
])

# Filter houses with more than four bedrooms
bedroom_condition = house_data[:, 0] > 4
houses_more_than_four_bedrooms = house_data[bedroom_condition]

# Calculate the average sale price
average_sale_price = np.mean(houses_more_than_four_bedrooms[:, 2])

# Print the result
print("Average Sale Price of Houses with More than Four Bedrooms:", average_sale_price)

