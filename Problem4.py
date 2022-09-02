"""
Given input
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24] """

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print("Length of set it_companies: ", len(it_companies))  # printing length of IT companies using len() method

# Add 'Twitter' to it_companies
it_companies.add("Twitter")  # adding 'Twitter' to IT companies set using add() function
print("\nSet of IT companies after adding Twitter: ", it_companies)  # printing IT companies set

# Insert multiple IT companies at once to the set it_companies
additional_companies = {'TATA', 'Infosys'}
it_companies.update(additional_companies)  # Inserting multiple IT companies using update() method
print("\nSet of IT companies after adding multiple companies: ", it_companies)  # printing IT companies set

# Remove one of the companies from the set it_companies
it_companies.pop()  # Remove one of the companies using pop() method
print("\nIT companies after removing one company: ", it_companies)  # printing IT companies set after removing one value

# What is the difference between remove and discard
"""
if the item which want to remove from the set not exist will raise error with remove() method 
if the item which want to remove from the set not exist will not raise error with discard() method 
"""

# Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

AB = A.union(B)  # joining A and B using union() method
print("\nJoin A and B: ", AB)  # printing AB set

# Find A intersection B
intersectionAB = A.intersection(B)  # intersection of A&B using intersection() method
print("\nA intersection B: ", intersectionAB)  # printing intersection of A and B

# Is A subset of B
if A.issubset(B):  # Checking A is subset of B or not using issubset() method
    print("\nA is subset of B")
else:
    print("\nA is not a subset of B")

# Are A and B disjoint sets
if A.isdisjoint(B):  # Checking A and B disjoint sets or not using isdisjoint() method
    print("\nA and B disjoint sets")
else:
    print("\nA and B are not a disjoint sets")

# Join A with B and B with A
A |= B
B |= A
print("\nAfter joining A with B: ", A)
print("\nAfter joining B with A: ", B)

# What is the symmetric difference between A and B
"""
The symmetric_difference() method will give us a set of values that are NOT present in both sets in common.
27, 28 are the symmetric difference between A and B. these are the only values that are not present in both sets(A and B) in common
example: a = {1,2,3}, b={3,4,5} Symmetric difference is {1,2,4,5} 
"""
ASB = A.symmetric_difference(B)
print("\nSymmetric difference between A and B: ", ASB)

# Delete the sets completely using del keyword
del it_companies
del A
del B
del AB
del intersectionAB
del ASB

# Convert the ages to a set and compare the length of the list and the set.
set_age = set(age)  # converting list age to set using set() method
print("\nAfter converting Age to set: ", set_age)  # printing set set_age

#  after converting to set duplicates are removed from list age
print("\nDifference between the length of the list and the set: ", len(age) - len(set_age))
