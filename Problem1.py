import statistics

# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()  # using sort() method to sort list
minAge = ages[0]  # min value without using min function list is in ascending order we can take first index for min Age
maxAge = ages[-1]  # max value without using max function list is in ascending order we can take last index for max Age
print("Sorted ages: ", ages)  # prints sorted list of ages
print("Minimum age: ", minAge)  # prints minimum age in ages list
print("Maximum age: ", maxAge)  # prints maximum age in ages list

# adding max and min ages to list
ages.append(minAge)  # adding minimum age to ages list using append() function
ages.append(maxAge)  # adding maximum age to ages list using append() function
print("\nList after adding min and max ages: ", ages)  # Printing ages list after adding min and max age

# median calculation
median_of_list = statistics.median(ages)  # finding median of age list using median() function in statistics library
print("\nMedian of ages list: ", median_of_list)  # printing median of ages list

# average age calculation
sumOfAges = 0
for x in ages:  # using for loop to get sum of ages in ages list
    sumOfAges += x
averageAge = sumOfAges / len(ages)  # finding average with formula avg= sum of ages/ no of ages
print("Average age: ", averageAge)  # printing average age

# Range of ages
rangeOfAges = maxAge - minAge  # finding average using formula avg = max - min
print("The range of the ages: ", rangeOfAges)  # printing range of ages list
