# Day 1 - 30DaysOfPython Challenge
import math
import sys

# 1. Check the python version you are using
print("Python version: " + sys.version.split()[0])
print("----------------------------")

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+), subtraction(-), multiplication(*), modulus(%), division(/), exponential(**), and floor division operator(//).

print("Addition 3 + 4: " + str(3+4))
print("Subtraction 3 - 4: " + str(3-4))
print("Multiplication 3 * 4: " + str(3*4))
print("Modulus 3 % 4: " + str(3%4))
print("Division 3 / 4: " + str(3/4))
print("Exponential 3 ** 4: " + str(3**4))
print("Floor division 3 // 4: " + str(3//4))
print("----------------------------")

# 3. Write strings on the python interactive shell. The strings are the following:
# Your name
# Your family name
# Your country
# I am enjoying 30 days of python

print("My name is David")
print("My family name is Molina")
print("My country is Catalonia")
print("I am enjoying 30 days of python")
print("----------------------------")

# 4. Check the data types of the following data:
# 10
# 9.8
# 3.14
# 4 -4j
# ['Asabeneh', 'Python', 'Finland']
# Your name
# Your family name
# Your country

print("10 is a " + str(type(10)))
print("9.8 is a " + str(type(9.8)))
print("3.14 is a " + str(type(3.14)))
print("4 - 4j is a " + str(type(4 - 4j)))
print("['Asabeneh', 'Python', 'Finland'] is a " + str(type(['Asabeneh', 'Python', 'Finland'])))
print("David is a " + str(type('David')))
print("Molina is a " + str(type('Molina')))
print("Catalonia is a " + str(type('Catalonia')))
print("----------------------------")

# 5. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

print("Integer: " + str(10))
print("Float: " + str(10.5))
print("Complex: " + str(10j))
print("String: " + str("Hello, World!"))
print("Boolean: " + str(True))
print("List: " + str([1, 2, 3]))
print("Tuple: " + str((1, 2, 3)))
print("Set: " + str({1, 2, 3}))
print("Dictionary: " + str({"name": "David", "age": 32, "country": "Catalonia"}))
print("----------------------------")

# 6. Find an Euclidian distance between (2, 3) and (4, 5). 

print("Euclidian distance between (2, 3) and (4, 5): " + str(math.sqrt((4-2)**2 + (5-3)**2)))
print("----------------------------")