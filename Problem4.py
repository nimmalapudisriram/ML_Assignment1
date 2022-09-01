"""
Given input
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24] """

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print("Length of set it_companies: ", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print("\nSet of IT companies after adding Twitter: ", it_companies)

# Insert multiple IT companies at once to the set it_companies
additional_companies = {'TATA', 'Infosys'}
it_companies.update(additional_companies)
print("\nSet of IT companies after adding multiple companies: ", it_companies)

# Remove one of the companies from the set it_companies
it_companies.pop()
print("\nIT companies after removing one company: ", it_companies)

# What is the difference between remove and discard
"""
if the item which want to remove from the set not exist will raise error with remove() method 
if the item which want to remove from the set not exist will not raise error with discard() method 
"""

# Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

AB= A.union(B)
print("\nJoin A and B: ", AB)

# Find A intersection B
intersectionAB = A.intersection(B)
print("\nA intersection B: ", intersectionAB)

# Is A subset of B
if (A.issubset(B)):
    print("\nA is subset of B")
else:
    print("\nA is not a subset of B")

# Are A and B disjoint sets
if (A.isdisjoint(B)):
    print("\nA and B disjoint sets")
else:
    print("\nA and B are not a disjoint sets")

# Join A with B and B with A
A |=B
B |=A
print("\nAfter joining A with B: ", A)
print("\nAfter joining B with A: ", B)

# What is the symmetric difference between A and B
"""
The symmetric_difference() method will give us a set of values that are NOT present in both sets in common.
27, 28 are the symmetric difference between A and B. these are the only values that are not present in both sets(A and B) in common
example: a = {1,2,3}, b={3,4,5} Symmetric difference is {1,2,4,5} there 
"""
ASB = A.symmetric_difference(B)
print("\nSymmetric difference between A and B: ", ASB)

# Delete the sets completely
del it_companies
del A
del B

# Convert the ages to a set and compare the length of the list and the set.
set_age = set(age)
print("\nAfter converting Age to set: ", set_age)
#  after converting to set duplicates are removed from list age
print("\nDifference between the length of the list and the set: ", len(age)-len(set_age))