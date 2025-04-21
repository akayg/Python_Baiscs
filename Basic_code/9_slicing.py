name= "abhishek_gore"
"""
This script demonstrates the concept of string slicing in Python.

String slicing allows you to extract a portion (substring) of a string by specifying a range of indices.
The general syntax for slicing is:
    string[start:stop:step]

- `start` (optional): The starting index of the slice (inclusive). Defaults to 0 if not provided.
- `stop` (optional): The ending index of the slice (exclusive). The slice will include characters up to, but not including, this index.
- `step` (optional): The step size or interval between indices. Defaults to 1 if not provided.
A
Key points about slicing:
1. If `start` is omitted, slicing starts from the beginning of the string.
2. If `stop` is omitted, slicing continues to the end of the string.
3. If `step` is omitted, the default step size is 1 (i.e., consecutive characters are selected).
4. A negative `step` can be used to reverse the string or slice in reverse order.
5. Out-of-range indices are handled gracefully; Python adjusts them to fit within the string's bounds.

Example:
    name = "abhishek_Gore"
    name[0:10]  # Extracts characters from index 0 to 9 (inclusive of 0, exclusive of 10).
    name[::2]   # Extracts every second character from the entire string.
    name[::-1]  # Reverses the string.

In this script, the slicing operation `name[0:10]` extracts the first 10 characters of the string `name`.
"""
print(name[0:10])

print(len(name))  # Prints the length of the string `name`
print(name.endswith("re"))  # Checks if the string `name` ends with the substring "re"
print(name.startswith("Go"))  # Checks if the string `name` starts with the substring "Go"
print(name.capitalize())  # Capitalizes the first character of the string `name`
print(name.upper())  # Converts all characters in the string `name` to uppercase
print(name.lower())  # Converts all characters in the string `name` to lowercase
print(name.find("shek"))  # Finds the first occurrence of the substring "shek" in `name`
print(name.replace("gore", "developer"))  # Replaces occurrences of "gore" with "developer" in `name`
print(name.split("_"))  # Splits the string `name` into a list using "_" as the delimiter
print(name.isalpha())  # Checks if all characters in the string `name` are alphabetic
print(name.isalnum())  # Checks if all characters in the string `name` are alphanumeric
print(name.strip("_"))  # Removes leading and trailing "_" characters from the string `name`