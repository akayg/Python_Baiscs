# Infinite loop to continuously prompt the user for input
while True:
    # Prompt the user to enter an odd number
    odd = int(input('Enter an odd number: '))
    
    # Check if the entered number is odd
    if odd % 2 == 1:
        # If the number is odd, print a confirmation message and exit the loop
        print(f"Number {odd} is odd")
        break
    else:
        # If the number is not odd, inform the user and prompt again
        print(f"Number {odd} is not odd. Try again.")