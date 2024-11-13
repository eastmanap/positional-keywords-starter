# Apollos Eastman
# Nov/13/2024
# Practice: Positional & Keyword Arguments in Python

import random
# POSITIONAL ARGUMENTS
# Start by writing the code to create the three functions outlined below
# You'll use only positional arguments in the first three functions
# Test your code and correct any errors

# Greet The User
# Write a function that takes two parameters -- first name and age
# Use an f-string to welcome the user by first name and to display his/her age
def greet(name,age):
    print(f'\nWelcome {name}!')
    print(f'You are {age}.\n')

greet(input('Enter your name:\n'), input('Enter your age:\n'))

# Area of a Rectangle
# Write a function to calculate the area (in square feet) of a rectangle
# Your two parameters will be length and width
# The print statement in the function should display the length, width and area (in square feet) of your rectangle
def rect_area(length,width):
    a = length*width
    return a

rect_input = int(input('\nEnter a number (1/2):\n'))
rect_input1 = int(input('Enter a second number (2/2):\n'))
print (f'The area of your rectangle is {rect_area(rect_input, rect_input1)}.')

# Sum of Numbers
# Write a function that finds the sum of three numbers
# Your three parameters will be num1, num2, and num3
# The print statement in the function should display the sum of the three numbers
def average(num1,num2,num3):
    a = (num1+num2+num3)/3
    return a

avg_input = int(input('\nEnter a number (1/3):\n'))
avg_input1 = int(input('Enter a second number (2/3):\n'))
avg_input2 = int(input('Enter a third number (3/3):\n'))
print (f'The average of your three numbers is {average(avg_input,avg_input1,avg_input2):.2f}.')

# KEYWORD ARGUMENTS
# Create the three functions outlined below
# In these last three functions, you'll use only keyword arguments 
# Test your code and correct any errors

# Greet By Title
# Write a function that greets the user by title, first name and last name
# Examples of titles include: Mr., Ms., Mrs. and Dr.
# When calling your function, change the order of your keyword arguments so that they don't match the order of your function parameters
def greet_title(first,last,title):
    print(f'\nHello {title} {first} {last}.')
    
titles = ['Mr.','Ms.','Mrs.','Dr.',]
greet_title(first = input('Enter your first name:\n'),last = input('Enter your last name:\n'), title = titles[random.randint(0,3)])

# Describe Your Pet
# Write a function that says what type of pet you have and what your pet's name is
# Your function parameters will be pet_type and pet_name
def pet_desc(pet_type,pet_name):
    print(f'\nYou have a pet {pet_type} named {pet_name}!')

pet_desc(pet_name = input('\nWhat is your pet\'s name:\n'),pet_type=input('What kind of animal is it?\n'))

# Updated Function
# Choose any ONE of the first three functions from this project and rewrite it below using keyword arguments
def greet(name,age):
    print(f'\nWelcome {name}!')
    print(f'You are {age}.\n')

greet(name = input('Enter your name:\n'), age = input('Enter your age:\n'))
