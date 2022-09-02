"""
Create a tuple containing names of your sisters and your brothers (imaginary siblings are
fine) """

brothers = ("Raghu", "Prem", "Manendra")  # created tuple with name brothers and added names
sisters = ("Bhavana", "Rangamma")  # created tuple with name sisters and added names
print("Brothers tuple: ", brothers)  # printing brothers tuple
print("Sisters tuple: ", sisters)  # printing sisters tuple

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters  # adding brothers and sisters tuples with '+' operator and assigning to siblings tuple
print("\nSiblings tuple with both brothers and sisters: ", siblings)  # Printing siblings tuple

# How many siblings do you have?
print("\nNo of siblings: ", len(siblings))  # Finding No. of siblings using len()

"""Modify the siblings tuple and add the name of your father and mother and assign it to 
family_members"""
father_name = "Satyam"
mother_name = "Uma devi"
siblings_list = list(siblings)  # converting siblings tuple to list using list() method
siblings_list.append(father_name)  # adding father name using append() function
siblings_list.append(mother_name)  # adding mother name using append() function
family_members = tuple(
    siblings_list)  # converting  list to tuple using tuple() method and assigning it to family_members
print("\nFamily members in tuple: ", family_members)  # printing family members names
