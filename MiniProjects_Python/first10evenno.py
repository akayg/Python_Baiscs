# Initialize the variable i to 1
i = 1

# Initialize a counter for even numbers
even_count = 0

# Loop until 10 even numbers are printed
while even_count < 10:
    # Check if the number is even
    if i % 2 == 0:
        # Print the even number
        print(i)
        # Increment the even number counter
        even_count += 1
    # Increment the value of i by 1
    i += 1