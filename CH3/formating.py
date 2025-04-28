letter = "Dear Harry,\n\tThis Python course is nice.\nThanks!"
print(letter)
# Adding a multi-line string using triple quotes
multi_line_string = """This is an example of a 
multi-line string in Python. 
It can span multiple lines."""
print(multi_line_string)

# Formatting a string using f-strings
name = "Harry"
course = "Python"
formatted_string = f"Hello {name}, welcome to the {course} course!"
print(formatted_string)

# Using string methods
upper_case = formatted_string.upper()  # Convert to uppercase
print(upper_case)

lower_case = formatted_string.lower()  # Convert to lowercase
print(lower_case)

# Replacing a word in the string
replaced_string = formatted_string.replace("Python", "JavaScript")
print(replaced_string)

# Splitting a string into a list
split_string = formatted_string.split()  # Splits by spaces by default
# Adding more examples with escape sequences
escaped_string = "This is a string with escape sequences:\n\t- Newline (\\n)\n\t- Tab (\\t)\n\t- Backslash (\\\\)\n\t- Single quote (\\')\n\t- Double quote (\\\")"
print(escaped_string)

# Printing the split string
print(split_string)