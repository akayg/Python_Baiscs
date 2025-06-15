# Define a list of numbers
nums = [1, 2, 3, 4, 5, 6]

# Use the map function with a lambda to calculate the square of each number in the list
square = map(lambda x: x**2, nums)

# Convert the map object to a list and print the squared numbers
print(list(square))