# Day 2: 30 Days of python programming

# Check the data type of all your variables using type() built-in function
# Using the len() built-in function, find the length of your first name
# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable total
# Subtract num_two from num_one and assign the value to a variable diff
# Multiply num_two and num_one and assign the value to a variable product
# Divide num_one by num_two and assign the value to a variable division
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
# Calculate num_one to the power of num_two and assign the value to a variable exp
# Find floor division of num_one by num_two and assign the value to a variable floor_division
# The radius of a circle is 30 meters.
    # Calculate the area of a circle and assign the value to a variable name of area_of_circle
    # Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords


house_hold_animal = 'cat'
first_name = 'kenny'
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two


user_input = int(input("enter radius: "))
radius = user_input
pi = 3.1416

area = pi * (radius ** 2)
circumference = ( pi * 2 ) * radius


first_name_dog = str(input("enter your dog first name: "))
last_name_dog = str(input("enter your dog last name: "))
country_of_dog = str(input("enter your dog origin: "))
age_of_dog = str(input("enter your dog age: "))

print(type(house_hold_animal))
print(len(first_name))
print(f'total {total}')
print(f'diff {diff}')
print(f'remainder {remainder}')
print(f'floor_division {floor_division}')
print(f'area = {area}')
print(f'circumference = {circumference}')


print('')

print(f'first name of the dog: {first_name_dog}')
print(f'last name of the dog: {last_name_dog}')
print(f'origin of the dog: {country_of_dog}')
print(f'age of the dog: {age_of_dog}')
help()