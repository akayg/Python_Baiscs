# Define a function to calculate the factorial of a number
def factorial(no):
    # Base case: factorial of 0 or 1 is 1
    if no == 0 or no == 1:
        return 1
    else:
        # Recursive case: multiply the number by the factorial of (number - 1)
        return no * factorial(no - 1)

# Prompt the user to enter a number
no = int(input("Enter a number: "))

# Check if the entered number is negative
if no < 0:
    # Factorial is not defined for negative numbers
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and display the factorial of the entered number
    print(f"The factorial of {no} is {factorial(no)}")