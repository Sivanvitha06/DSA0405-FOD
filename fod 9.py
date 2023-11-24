import matplotlib.pyplot as plt

# Assuming you have a dataset with month names and corresponding sales values
# Example data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales_values = [10000, 12000, 9000, 15000, 11000]

# Create a line plot
plt.figure(figsize=(8, 5))  # Adjust the figure size if needed
plt.plot(months, sales_values, marker='o', linestyle='-', color='b', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.legend()
plt.grid(True)
plt.show()

