import pandas as pd
import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd  
import matplotlib.pyplot 

# Assuming order_data is your DataFrame


data = {
    'customer_id': [1, 2, 1, 3, 2, 1, 3],
    'order_date': ['2023-01-15', '2023-01-16', '2023-01-17', '2023-01-15', '2023-01-16', '2023-01-18', '2023-01-19'],
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'order_quantity': [3, 2, 1, 4, 3, 2, 5]
}

order_data = pd.DataFrame(data)

# Convert 'order_date' column to datetime type
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# Display the order_data DataFrame
print(order_data)




# 1. Total number of orders made by each customer
total_orders_per_customer = order_data.groupby('customer_id')['order_date'].count()

# 2. Average order quantity for each product
average_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

# 3. Earliest and latest order dates in the dataset
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

# Display the results
print("Total number of orders made by each customer:")
print(total_orders_per_customer)

print("\nAverage order quantity for each product:")
print(average_quantity_per_product)

print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
