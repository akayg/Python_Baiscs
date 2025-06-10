import math_utl  # Importing a custom module named math_utl (ensure math_utl.py exists in the same directory)

# Prompt the user to input the first number
number = int(input("Enter first number: "))

# Prompt the user to choose an operation
operation = input("Choose operation:\n  a - Sum\n  b - Square\n  c - Division\nYour choice: ")

# Check if the selected operation is 'b' (Square)
if operation == 'b':
    # Call the square function from math_utl and print the result
    print("Square:", math_utl.square(number))

# Check if the selected operation is either 'a' (Sum) or 'c' (Division)
elif operation in ['a', 'c']:
    # Prompt the user to input the second number
    number2 = int(input("Enter second number: "))

    # If the operation is 'a', calculate and print the sum
    if operation == 'a':
        print("Sum:", math_utl.sum(number, number2))
    # If the operation is 'c', perform division
    elif operation == 'c':
        # Check if the second number is zero to avoid division by zero
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            # Call the divide function from math_utl and print the result
            print("Division:", math_utl.divide(number, number2))
# Handle invalid operation input
else:
    print("Invalid operation selected.")
