# You are organizing participants for three different workshops in a coding bootcamp: Web Development, Data Science, and UI/UX Design.
# Create a list for each workshop containing the names of 3 participants.
# Combine all three workshop lists into a single nested list called all_participants.
# A new participant joins the Web Development workshop — add their name to that list.
# Insert one more participant at the 2nd position in the Data Science list.
# Remove the last participant from the UI/UX Design list.
# Copy the list of Data Science participants to a new list and clear the original.
# From the Web Development list, display only the first two participants.
# Use list comprehension to create a list of the length of each name in the copied Data Science list.
# Check whether “Asha” is in any of the workshop lists.
# Finally, create a tuple that stores the name of the first participant from each workshop list (use slicing and indexing as needed).

web_development = ["Sam","Zam","Ram"]
data_science = ["John","Paul","Pogba"]
UI_UX_Design = ["Pedri","Gavi","Xavi"]

all_participants = [web_development,data_science,UI_UX_Design]
print("Nested List : ",all_participants)

web_development.append("drogba")
print("After appending a new name : ",web_development)
data_science.insert(1,"jam")
print("After inserting a new name at 2nd pos : ",data_science)
UI_UX_Design.pop()
print("After removing the last name : ",UI_UX_Design)

new_DS_list = data_science.copy()
data_science.clear()

print("First two participants : ",web_development[0:2])

lengths = [len(x) for x in new_DS_list]
print("Lengths of each name in new DS list : ",lengths)

if "Asha" in web_development + new_DS_list + UI_UX_Design:
    print("Asha present in the workshops")
else:
    print("Asha not present in any of the workshops")

first_participant = (web_development[0],new_DS_list[0],UI_UX_Design[0])
print("First participant tuple : ",first_participant)



