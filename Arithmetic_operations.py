# Calculator in Python

# Taking input from the user for the first number.
# The input() function returns a string, so we convert
num1 = int(input("Type here a first number : "))

# Taking input from the user for the second number.
# Again, converting input string to integer.
num2 =  int(input("Type here a second number : "))

# Taking input from the user for the operator
# The operator is kept as a string, e.g., "+", "-", "*", "/", "%", "**", "//"
Operator = input("Choose an operator (+, -, *, /, %, **, //): ")

# Using conditional statements to perform the correct operation based on the operator entered.

if Operator == "+":
    # Addition operation.
    print("Result:", num1 + num2)

elif Operator == "-":
    # Subtraction operation.
    print("Result:", num1 - num2)

elif Operator == "*":
    # Multiplication oper.ation
    print("Result:", num1 * num2)

elif Operator == "/":
    # Division operation.
    # Check to make sure we are not dividing by zero.
    if num2 != 0:
        print("Result:", num1 / num2)  # Regular division (float result).
    else:
        print("Error: Division by zero is not allowed")

elif Operator == "//":
    # Floor division operation (division without remainder, returns integer).
    if num2 != 0:
        print("Result:", num1 // num2)
    else:
        print("Error: Division by zero is not allowed")

elif Operator == "%":
    # Modulus operation (returns the remainder of division).
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Error: Division by zero is not allowed")

elif Operator == "**":
    # Exponentiation operation (Num1 raised to the power of Num2).
    print("Result:", num1 ** num2)

else:
    # If the user enters an operator not listed above.
    print("Invalid operator entered. Please choose a valid one.")
