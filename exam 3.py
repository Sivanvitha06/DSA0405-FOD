import pandas as pd
from scipy.stats import t
import numpy as np

# Read the CSV file
df = pd.read_csv("customer_reviews.csv")

# Assuming your CSV has a column named 'rating' that contains customer ratings
ratings = df['rating']

# Calculate the mean and standard deviation of ratings
mean_rating = ratings.mean()
std_dev = ratings.std()

# Calculate the sample size and degrees of freedom
sample_size = len(ratings)
degrees_of_freedom = sample_size - 1

# Set the confidence level (e.g., 95%)
confidence_level = 0.95

# Calculate the critical value for a two-tailed test
t_critical = t.ppf((1 + confidence_level) / 2, degrees_of_freedom)

# Calculate the margin of error
margin_of_error = t_critical * (std_dev / np.sqrt(sample_size))

# Calculate the confidence interval
confidence_interval = (mean_rating - margin_of_error, mean_rating + margin_of_error)

# Print the results
print(f"Mean Rating: {mean_rating}")
print(f"Standard Deviation: {std_dev}")
print(f"Confidence Interval ({confidence_level * 100}%): {confidence_interval}")
