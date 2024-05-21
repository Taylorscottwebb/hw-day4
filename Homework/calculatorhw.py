response = input("Would you like to add, subtract, multiply, or divide?")
num1 = float(input("Enter first number here: "))
num2 = float(input("Enter second number here: "))

if response == "add":
    result = num1 + num2
    print(result)
elif response == "subtract":
    result = num1 - num2
    print(result)
elif response == "multiply":
    result = num1 * num2
    print(result)
elif response == "divide":
    if num2 == 0:
        print("INVALID, cannot divide by zero")
    else:
        result = num1 / num2
        print(result)
else:
 print("Invalid input try again")




