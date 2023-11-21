item_prices = [2.50, 3.75, 1.20, 5.00]
quantities = [3, 2, 4, 1]
discount_rate = 10  # 10% discount
tax_rate = 7       # 7% tax

# Calculate the total cost before discounts and taxes
subtotal = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))

# Calculate the discount amount
discount_amount = (discount_rate / 100) * subtotal

# Apply the discount
total_after_discount = subtotal - discount_amount

# Calculate the tax amount
tax_amount = (tax_rate / 100) * total_after_discount

# Calculate the final total cost
final_total_cost = total_after_discount + tax_amount

# Display the results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${discount_amount:.2f}")
print(f"Total after discount: ${total_after_discount:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Final Total Cost: ${final_total_cost:.2f}")
