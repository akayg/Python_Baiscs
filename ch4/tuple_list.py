# Example of a list
friends = ['abhishek', False, 9]  # Lists are ordered, mutable, and can contain elements of different data types
print(type(friends))
# Tuples are similar to lists but are immutable (cannot be changed after creation)
# Example of a tuple
friends_tuple = ('abhishek', False, 9)
print(type(friends_tuple))

# Lists are mutable, meaning we can modify them
friends[1] = True  # Modifying the list
print(friends)

# Tuples, on the other hand, cannot be modified
try:
    friends_tuple[1] = True  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")