import numpy as np

# Assuming 'sales_data' is a NumPy array with a column representing the prices of the products
# Load your dataset into 'sales_data' accordingly

# Example data (replace this with your actual data)
sales_data = np.array([50.0, 30.0, 45.0, 60.0, 25.0])

# Calculate the average price
average_price = np.mean(sales_data)

# Print the result
print("Average Price of Products Sold in the Past Month:", average_price)
