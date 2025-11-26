# Write a Python program that does the following:
# Store a short paragraph about a Python course using a multiline string.
# Display the length of the paragraph (number of characters).
# Display the first and last characters in the paragraph.
# Slice and print a short preview: the first 50 characters.
# Replace all occurrences of the word "Python" with "PYTHON" (in all caps).
# Convert the entire paragraph to lowercase.
# Remove any extra whitespaces from the start or end.
# Split the paragraph into individual words and print the list.
# Check if the word "course" exists in the paragraph. Print a message if found.
# Display the final message:
# "The course description is {} characters long and has {} words." using the format() method.

course = """    Python is an interpreted, 
high-level and general-purpose programming language.
Python is an object-oriented language too,
which simply means it can model entities in the real world.     """

length = len(course)
print("The length of the paragraph is : ",length)

first_char = course[0]
print("First char : ",first_char)

last_char = course[-1]
print("Last char : ",last_char)

slice_para = course[:50]
print("The first 50 characters : ",slice_para)

replacing = course.replace("Python","PYTHON")
print("The para after replacement : ",replacing)

lower_case = course.lower()
print("Lower cased : ",lower_case)

white_space = course.strip()
print("After removing white spaces : ",white_space)

split_para = course.split()
print("After spliting : ",split_para)

if "course" in course:
    print("The word 'course' is Found")
else:
    print("The word 'course' Not Found")

final_characters = len(white_space)
final_words = len(split_para)
message = "The course description is {} characters long and has {} words."
final_msg = message.format(final_characters,final_words)
print(final_msg)

