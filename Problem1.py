import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minAge = ages[0]     # min value without using min function list is in ascending order
maxAge = ages[-1]    # max value without using max function
print("Sorted ages: ", ages)
print("Minimum age: ", minAge)
print("Maximum age: ", maxAge)

# adding max and min ages to list
ages.append(minAge)
ages.append(maxAge)
print("\nList after adding min and max ages: ", ages)

# median calculation
median_of_list= statistics.median(ages)
print("\nMedian of ages list: ", median_of_list)


# average age calculation
sumOfAges=0
for x in ages:
    sumOfAges += x

averageAge = sumOfAges / len(ages)
print("Average age: ", averageAge)


# Range of ages
rangeOfAges = maxAge - minAge
print("The range of the ages: ", rangeOfAges)