import pandas  as  pd

data = {
    'Property_ID': [1, 2, 3, 4, 5],
    'Location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'Bedrooms': [3, 4, 3, 5, 2],
    'Area_SqFt': [1500, 1800, 1600, 2200, 1200],
    'Listing_Price': [250000, 300000, 280000, 400000, 200000]
}

property_data = pd.DataFrame(data)

# 1. The average listing price of properties in each location
average_listing_price_per_location = property_data.groupby('Location')['Listing_Price'].mean()

# 2. The number of properties with more than four bedrooms
properties_more_than_four_bedrooms = property_data[property_data['Bedrooms'] > 4].shape[0]

# 3. The property with the largest area
property_with_largest_area = property_data.loc[property_data['Area_SqFt'].idxmax()]

# Display the results
print("Average listing price of properties in each location:")
print(average_listing_price_per_location)

print("\nNumber of properties with more than four bedrooms:", properties_more_than_four_bedrooms)

print("\nProperty with the largest area:")
print(property_with_largest_area)
