# Initialize the variable `i` to 1, which will be used as a counter in the loop
i = 1

# Prompt the user to input a number `n` and convert it to an integer
n = int(input("Enter number: "))

# Initialize the variable `sum` to 0, which will store the cumulative sum
sum = 0

# Start a while loop that will run as long as `i` is less than or equal to `n`
while i <= n:
    # Check if the current value of `i` is divisible by 5
    if i % 5 == 0:
        # If `i` is divisible by 5, increment `i` by 1 and skip the rest of the loop
        i += 1
        continue
    
    # Add the current value of `i` to the `sum` variable
    sum += i
    
    # Increment `i` by 1 to move to the next number
    i += 1

# After the loop ends, print the final value of `sum`
print("The sum is:", sum)
