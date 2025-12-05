# You are helping a shopper manage their grocery shopping list. Your task is to create a simple Python program that does the following steps in order:

# Initial Grocery List:
# Create a list with the initial items: ["milk", "bread", "eggs"].
# Add Item Function:
#   Write a function add_item(item) that adds a given item (string) to the grocery list.
# Remove Last Item Function:
#   Write a function remove_last_item() that removes the last item from the grocery list.
# Lambda Function for Display:
# Use a lambda function to print each item in the list with the format: "Item: <item>".
# Recursive Character Count (Bonus):
# Write a recursive function count_characters(items) that returns the total number of characters in all item names combined. 
# For example, ["milk", "bread"] has 4 + 5 = 9 characters..

grocery_items = ["milk", "bread", "eggs"]
def add_item(item):
    grocery_items.append(item)
    print(f"{item} added to list")


add_item("chocolate")
print(f"{grocery_items}")

def remove_last_item():
    if len(grocery_items) > 0:
        removed_item = grocery_items.pop()
        return removed_item
    else:
         return "List is empty"
    
removed = remove_last_item()
print(f"Removed {removed}")

print_item = lambda x : print(f"Item : {x}")
for item in grocery_items:
      print_item(item)

def count_characters(items):
      if len(items) == 0:
       return 0
 
      first_word_length = len(items[0])
      rest_of_list = count_characters(items[1:])
      return first_word_length + rest_of_list

total = count_characters(grocery_items)
print(f"total characters in the list : {total}")
 
    
