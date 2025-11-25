# A juice shop sells three types of drinks: apple, orange, and grape. You are asked to calculate the total volume of juice sold in one day.
# The shop sold:
# 15.5 liters of apple juice
# 20 liters of orange juice
# 10.25 liters of grape juice
# Your task:
# Store the volume of each juice in separate variables.
# Calculate the total volume sold.
# Print the total volume.
# Convert the total volume to an integer and print it.
# Convert the total volume to a string and print it with a message.
# Add a random number between 5 and 10 (representing additional bonus liters) and print the final total

import random

apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25

total_sold = apple_juice + orange_juice + grape_juice

print("Total volume sold = ",total_sold)

total_int = int(total_sold)
print ("type: ",type(total_int))

total_str = str(total_int)
print ("The total volume sold is converted to string",total_str)

additional_liters = total_int + random.randrange(5,10)
print ("The volume with bonus liters",additional_liters)