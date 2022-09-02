radius = 30
# Calculate the area of a circle and assign the value to a variable name of _area_of_circle_

PI = 3.14159265359
_area_of_circle_ = PI * radius * radius  # calculating area of circle using formula
print("The area of a circle: {:.2f} meters square".format(_area_of_circle_))  # printing area of circle

# Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
_circum_of_circle_ = 2 * PI * radius  # calculating perimeter of circle using formula
print("\nThe circumference of a circle: {:.2f} meters".format(_circum_of_circle_))  # printing perimeter of circle

user_radius = float(input("\nEnter the radius of a circle:"))  # Taking radius input from the user
_area_of_circle_ = PI * user_radius * user_radius  # calculating area of circle using formula
print("\nThe area of a circle with user input radius: {:.2f} meters square".format(_area_of_circle_))
