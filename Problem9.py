"""Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
kilograms in a separate list using Loop. N: No of students (Read input from user)"""

weights = []
no_of_students = int(input("Enter no of students: "))  # Taking No. of students input from user
print("\nEnter student weights in lbs: ")  # printing message
for i in range(0, no_of_students):  # for loop take inputs from user in lbs through console
    lbs = int(input())
    weights.append(lbs)

weight_kgs = []
for i in range(0, no_of_students):  # for loop to convert weights from lbs to kgs
    kgs = 0.453592 * weights[i]  # multiplication of 0.453592 with lbs will give kgs
    weight_kgs.append(round(kgs, 2))  # adding weight in kgs to new list

print("\nweights of students in lbs: ", weights)  # printing weights in lbs
print("\nweights of students in kilograms: ", weight_kgs)  # printing weights in kgs
