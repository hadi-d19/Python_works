# Homework Problem:
# A grocery store wants to calculate the final bill for a customer. The store has 3 products: rice, sugar, and oil.
# Each product has a fixed price per kilogram:
# Rice: ?45 per kg
# Sugar: ?40 per kg
# Oil: ?130 per kg
# Assume a customer bought:
# 3 kg of rice
# 2.5 kg of sugar
# 1.8 kg of oil
# Your task:
# Use variables to store the prices and quantities.
# Use appropriate data types.
# Calculate and print the total price for each item and the final total bill.
# Show the total bill as an integer and also as a string.
# Convert the float values where needed using explicit conversion.
# Use random number generation to add a random ?5–?10 delivery charge.
# Show the final bill amount including delivery charge.

import random

rice_price = 45
sugar_price = 40
oil_price = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

total_rice = rice_price * rice_qty
total_sugar = sugar_price * sugar_qty
total_oil = oil_price * oil_qty

print("Total price of rice = ",total_rice)
print("Total price of sugar = ",total_sugar)
print("Total price of oil = ",total_oil)

final_bill = total_rice + total_sugar + total_oil
print("The Final bill = ",final_bill)

final_int = int(final_bill)
print ("The final bill in int = ",final_int)

final_str = str(final_int)
print ("The final bill in str is ",final_str)

added_delivery_charge = final_int + random.randrange(5,11)
print("Final bill including delivery charge = ",added_delivery_charge)
