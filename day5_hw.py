# You are managing an online course portal that keeps track of student enrollments in two subjects: "Frontend" and "Backend".
# Create two sets:
# One with the names of students enrolled in the Frontend course
# One with the names of students enrolled in the Backend course
# Perform the following tasks:
# Add a new student to the Backend course
# Remove a student from the Frontend course
# Display the list of students who are enrolled in both courses
# Display the list of students who are enrolled only in Backend, but not in Frontend
# Display the total number of unique students
# Create a dictionary where:
# Keys are course names ("Frontend", "Backend")
# Values are the number of students enrolled in each
# Print each course name with the number of students using a loop
# Using dictionary comprehension, create a new dictionary that adds a "Fullstack" course by combining student counts
# from both existing courses.

Frontend = {"Zam","Paul","John","Xavi","Iniesta"}
Backend = {"Zam","Pedri","Gavi","Paul"}

Backend.add("Pogba")
Frontend.remove("Xavi")

both_courses = Frontend.intersection(Backend)
print("The students enrolled in both courses : ",both_courses)

only_Backend = Backend - Frontend
print("The students enrolled in Backend only : ",only_Backend)

unique_students = len(Frontend | Backend)
print("The total number of unique students: ",unique_students)

course_counts = {
    "Frontend" : len(Frontend),
    "Backend" : len(Backend)
}
for x,y in course_counts.items():
    print(f"Course : {x}, Students : {y}")

final_report = {k: v for k,v in course_counts.items()}
final_report["Fullstack"] = course_counts["Frontend"] + course_counts["Backend"]
print("Final report with Fullstack : ",final_report)


