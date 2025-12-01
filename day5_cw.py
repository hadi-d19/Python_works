# you are creating a basic system to manage students enrolled in various courses.
# Create two sets: one for students enrolled in "Python" and one for "Data Science".
# Add a new student to the Python set.
# Remove one student from the Data Science set.
# Find and display the names of students who are enrolled in both courses.
# Find students who are only in the Python course but not in Data Science.
# Display the combined list of all students in either course (no duplicates).
# Create a dictionary with course names as keys and number of students as values.
# Using a loop, print the course name and number of students in the format:
# Course: Python, Students: 3
# Using dictionary comprehension, create a new dictionary where course names are unchanged, but values are doubled 
# (to simulate expected growth)

Python = {"Zam","Sam","Ram","Pedri"}
Data_Science = {"Zam","Pedri","Gavi","Xavi"}

Python.add("Jam")
print("Added student : ",Python)
Data_Science.pop()
print("Removed a student : ",Data_Science)

both_courses = Python.intersection(Data_Science)
print("Students enrolled in both Courses : ",both_courses)

only_Python = Python-Data_Science
print("Students enrolled in python only : ",only_Python)

combined_list = Python.union(Data_Science)
print("Students enrolled in either of the courses : ",combined_list)

course_counts = {
    "Python" : len(Python),
    "Data Science" : len(Data_Science)
}
print("\nInitial Dictionary : ",course_counts)

for x,y in course_counts.items():
    print(f"Course : {x}, Students : {y}")

doubled_values = {k: v*2 for k,v in course_counts.items()}
print("Names unchanged with doubled values : ",doubled_values)