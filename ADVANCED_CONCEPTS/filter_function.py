# Define a list of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use the filter function with a lambda to filter even numbers from the list
even = filter(lambda x: x % 2 == 0, nums)

# Print the filtered even numbers
print(f"Even numbers are {list(even)}")