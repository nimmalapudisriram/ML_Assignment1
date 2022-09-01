"""Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
kilograms in a separate list using Loop. N: No of students (Read input from user)"""

weights = []
no_of_students = int(input("Enter no of students: "))
print("\nEnter student weights in Ils: ")
for i in range(0, no_of_students):
    lbs=int(input())
    weights.append(lbs)

weight_kgs = []
for i in range(0, no_of_students):
    kgs = 0.453592 * weights[i]
    weight_kgs.append(round(kgs, 2))

print(weight_kgs)
