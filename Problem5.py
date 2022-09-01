radius = 30
# Calculate the area of a circle and assign the value to a variable name of _area_of_circle_

PI = 3.14159265359
_area_of_circle_  = PI * radius * radius
print("The area of a circle: {} meters square".format(_area_of_circle_))

# Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
_circum_of_circle_ = 2 * PI * radius
print("\nThe circumference of a circle: {} meters".format(_circum_of_circle_))

user_radius = float(input("\nEnter the radius of a circle:"))
_area_of_circle_ = PI * user_radius * user_radius
print("\nThe area of a circle with user input radius: {} meters square".format(_area_of_circle_))

