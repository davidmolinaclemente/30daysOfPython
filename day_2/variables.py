# Day 2 - 30DaysOfPython Challenge

## Exercises: Level 1

# 2. Write a python comment saying 'Day 2: 30 Days Of Python programming'

import math


print("Day 2: 30 Days Of Python programming")

# 3. Declare a first name variable and assign a value to it

first_name = "David"
print(first_name)

# 4. Declare a last name variable and assign a value to it

last_name = "Molina"
print(last_name)

# 5. Declare a full name variable and assign it a value

full_name = first_name + " " + last_name
print(full_name)

# 6. Declare a country variable and assign it a value to it

country = "Catalonia"
print(country)

# 7. Declare a city variable and assign it a value to it

city = "Barcelona"
print(city)

# 8. Declare an age variable and assign it a value to it

age = 32
print(age)

# 9. Declare a year variable and assign it a value to it

year = 2025
print(year)

# 10. Declare a variable is_married and assign it a value to it

is_married = False
print(is_married)

# 11. Declare a variable is_true and assign a value to it

is_true = True
print(is_true)

# 12. Declare a variable is_light_on and assign it a value to it

is_light_on = True
print(is_light_on)

# 13. Declare multiple variables in one line

pet_name, pet_age, pet_type = "Leia", 4, "dog"
print(pet_name, pet_age, pet_type)
print("----------------------------")

## Exercises: Level 2

# 1. Check the data type of all your variables using type() built-in function

print("first_name is a " + str(type(first_name)))
print("last_name is a " + str(type(last_name)))
print("full_name is a " + str(type(full_name)))
print("country is a " + str(type(country)))
print("city is a " + str(type(city)))
print("age is a " + str(type(age)))
print("year is a " + str(type(year)))
print("is_married is a " + str(type(is_married)))
print("is_true is a " + str(type(is_true)))
print("is_light_on is a " + str(type(is_light_on)))
print("pet_name is a " + str(type(pet_name)))
print("pet_age is a " + str(type(pet_age)))
print("pet_type is a " + str(type(pet_type)))

# 2. Using the len() built-in function, find the length of your first name

print("The length of first_name is " + str(len(first_name)))

# 3. Compare the length of your first name and your last name

print("The length of first_name is equal to the length of last_name: " + str(len(first_name) == len(last_name)))

# 4. Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

# 5. Add num_one and num_two and assign the value to a variable total

total = num_one + num_two
print("The total of num_one and num_two is " + str(total))

# 6. Subtract num_two from num_one and assign the value to a variable diff

diff = num_one - num_two
print("The difference of num_one and num_two is " + str(diff))

# 7. Multiply num_two and num_one and assign the value to a variable product

product = num_two * num_one
print("The product of num_two and num_one is " + str(product))

# 8. Divide num_one by num_two and assign the value to a variable division

division = num_one / num_two
print("The division of num_one and num_two is " + str(division))

#9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

remainder = num_two % num_one
print("The remainder of num_two divided by num_one is " + str(remainder))

#10. Calculate num_one to the power of num_two and assign it to a variable exp

exp = num_one ** num_two
print("The exponent of num_one to the power of num_two is " + str(exp))

#11. Find the floor division of num_one by num_two and assign it to a variable floor_division

floor_division = num_one // num_two
print("The floor division of num_one and num_two is " + str(floor_division))

#12. The radios of a circle is 30 meters.
#i. Calculate the area of a circle and assign it to a variable area_of_circle
#ii. Calculate the circumference of a circle and assign it to a variable circumference_of_circle
#iii. Take radius as user input and calculate the area.

area_of_circle = 30 ** 2 * math.pi
circumference_of_circle = 2 * 30 * math.pi
print("The area of the circle is " + str(area_of_circle))
print("The circumference of the circle is " + str(circumference_of_circle))

user_radius = input("Enter the radius of the circle: ")

try:
    user_radius = float(user_radius)
except ValueError:
    print("The radius should be a float number, not a " + str(type(user_radius)) + ". Please try again.")
    exit()

if user_radius < 0:
    print("The radius is not a positive number. Please try again.")
    exit()
else:
    area_of_circle = float(user_radius) ** 2 * math.pi

print("The area of the circle is " + str(area_of_circle))

#13. Use the built-in input() method to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print("Your first name is " + first_name)
print("Your last name is " + last_name)
print("Your country is " + country)
print("Your age is " + age)

#14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

help('keywords')