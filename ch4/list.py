#this is a list which is muteable
alpha = ["Abhishek","Gore", False , 92]
print(type(alpha))
print(alpha[1])
print(alpha[0:3])
alpha.append(18291)
print(alpha)
alpha.reverse()
print(alpha)
# Access and print the second element of the list
# The second element is at index 1 (0-based indexing)
print(alpha[1])
