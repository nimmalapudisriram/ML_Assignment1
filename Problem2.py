# Creating empty dictionary
dog = {}
print("Dog empty dictionary: ", dog)

# Add name, color, breed, legs, age to the dog dictionary

dog = {
    "Name" : "Sony",
    "color": "Light Golden",
    "bread": "Golden Retriever",
    "legs" : 4,
    "age"  : 3
}
print("\nDetails of dog: ", dog)

"""Create a student dictionary and add first_name, last_name, gender, age, marital status, 
skills, country, city and address as keys for the dictionary"""

Student = {
    "first_name" : "Sri Ram",
    "last_name"  : "Nimmalapudi",
    "gender"     : "male",
    "age"        : 22,
"marital status" : "unmarried",
    "skills"     : ["Critical thinking", "Verbal Communication"],
    "country"    : "India",
    "city"       : "Vijayawada",
    "address"    : "2-354/3, Muchinapalli, Andhra Pradesh, Pin:521215"
}
print("\nStudent details: ", Student)

# Get the length of the student dictionary
student_length = len(Student)
print("\nStudent dictionary length: ", student_length)

# Get the value of skills and check the data type, it should be a list
print("\nValue of skills key: ", Student["skills"])
print("\nSkills key values data type: ", type(Student["skills"]))

# Modify the skills values by adding one or two skills
Student["skills"].append("Leadership")
print("\nAfter modification Value of skills key: ", Student["skills"])

# Get the dictionary keys as a list
keys_list = list(Student.keys())
print("\nList of all keys in student dictionary: ", keys_list)

# Get the dictionary values as a list
values_list = list(Student.values())
print("\nList of all values in student dictionary: ", values_list)

