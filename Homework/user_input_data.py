# 2. User Input Data Processor
# Objective: The 
# aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator Write a script that checks the length of the user's first name and last name.
# Both should be at least 2 characters long. If not, print an error message.

first_name = input("Your first name:  ") 
last_name = input("Your last name is :  ")
user_name = first_name + last_name
count =len(first_name)

if count <= 2 :
    print("This is a invalid name...")
else: print(first_name)

count = len(last_name)

if count <= 2 :
    print("This is a invalid name...")
else: print(last_name)

