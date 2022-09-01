"""
Create a tuple containing names of your sisters and your brothers (imaginary siblings are
fine) """

brothers = ("Raghu", "Prem", "Manendra")
sisters = ("Bhavana", "Rangamma")
print("Brothers tuple: ", brothers)
print("Sisters tuple: ", sisters)

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print("\nSiblings tuple with both brothers and sisters: " ,siblings)

# How many siblings do you have?
print("\nNo of siblings: ", len(siblings))

"""Modify the siblings tuple and add the name of your father and mother and assign it to 
family_members"""
father_name = "Satyam"
mother_name = "Uma devi"
siblings_list = list(siblings)
siblings_list.append(father_name)
siblings_list.append(mother_name)
family_members = tuple(siblings_list)
print("\nFamily members in tuple: ", family_members)