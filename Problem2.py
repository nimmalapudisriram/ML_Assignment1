# Creating empty dictionary
dog = {}  # created empty dictionary with name dog
print("Dog empty dictionary: ", dog)  # printing  empty dog dictionary

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    "Name": "Sony",
    "color": "Light Golden",
    "bread": "Golden Retriever",
    "legs": 4,
    "age": 3
}  # given values to name, color, breed, legs, age to the dog dictionary
print("\nDetails of dog: ", dog)  # printing dog details using dictionary

"""Create a student dictionary and add first_name, last_name, gender, age, marital status, 
skills, country, city and address as keys for the dictionary"""
student = {
    "first_name": "Sri Ram",
    "last_name": "Nimmalapudi",
    "gender": "male",
    "age": 22,
    "marital status": "unmarried",
    "skills": ["Critical thinking", "Verbal Communication"],
    "country": "India",
    "city": "Vijayawada",
    "address": "2-354/3, Muchinapalli, Andhra Pradesh, Pin:521215"
}  # created student dictionary with key, values pairs
print("\nStudent details: ", student)  # printing student dictionary

# Get the length of the student dictionary
student_length = len(student)  # finding length  of student dictionary with len() function
print("\nStudent dictionary length: ", student_length)  # printing student dictionary length

# Get the value of skills and check the data type, it should be a list
print("\nValue of skills key: ",
      student["skills"])  # printing the value of skills key in student dictionary using index
print("\nSkills key values data type: ",
      type(student["skills"]))  # printing the data type of skills key in student dictionary type() function

# Modify the skills values by adding one or two skills
student["skills"].append("Leadership")  # adding value to skills values using append() function
print("\nAfter modification Value of skills key: ",
      student["skills"])  # printing skills key values in student dictionary

# Get the dictionary keys as a list
keys_list = list(student.keys())  # extracting keys in student dictionary using keys() function
print("\nList of all keys in student dictionary: ", keys_list)  # printing keys in student dictionary

# Get the dictionary values as a list
values_list = list(student.values())  # extracting values in student dictionary using values() function
print("\nList of all values in student dictionary: ", values_list)  # printing values in student dictionary
