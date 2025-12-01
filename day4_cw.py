#  You are managing a small grocery store. You keep lists of items sold in three sections: fruits, vegetables, and beverages.
# Create separate lists for each section with at least 3 items.
# Add a new item to the fruits list.
# Insert a new item at the second position of the vegetables list.
# Remove the last item from the beverages list.
# Combine all three lists into a nested list called inventory.
# Use slicing to print only the first two fruits.
# Use negative indexing to access the last item from the vegetables list.
# Create a list of lengths of all items in the fruits list using list comprehension.
# Check if "Water" is in the beverages list.
# Finally, create a tuple of the first item from each section.
# .

fruits = ["apple","banana","orange"]
vegetables = ["cucumber","carrot","onion"]
beverages =  ["water","pepsi","sprite"]

fruits.append("mango")
vegetables.insert(1,"tomato")
beverages.pop()

inventory = [fruits,vegetables,beverages]
print("Nested Inventory",inventory)

print("The first 2 fruits : ",fruits[0:2])
print("The last element : ",vegetables[-1])

lengths = [len(x) for x in fruits]
print(lengths)

if "water" in beverages:
    print("water is present in beverages")
else:
    print("water is not present in beverages")

first_items = (fruits[0],vegetables[0],beverages[0])
print("First items tuple : ",first_items)