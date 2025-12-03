# You are working on a simple attendance tracking system for a 5-day workshop. You have a list of the number of students present
# each day:
# attendance = [18, 20, 19, 15, 21]
# Your tasks are:
# Loop through the list and print whether the class was "Full" if 20 or more students were present, or "Not Full" otherwise.
# Count how many days the class was full.
# Calculate and print the total attendance for all 5 days.

attendance = [18,20,19,15,21]
full_days_count = 0
total_attendance =0

for x in attendance :
    total_attendance+=x

    if x >= 20:
        print("The class was full : ",x)
        full_days_count +=1
    else:
        print("The class was not full : ",x)

print("The number of days the class was full : ",full_days_count)
print("The total attendance for 5 days : ",total_attendance)
