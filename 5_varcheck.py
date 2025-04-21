#in this code we'll check what in datatype of inout var

# a=input('input data')
# t = type(a)
# print (t)

# but the above code will only return STR as it take it as str for every input

user_input = input("Enter something: ")

# Try converting to int
try:
    user_input = int(user_input)
except ValueError:
    # If not int, try float
    try:
        user_input = float(user_input)
    except ValueError:
        pass  # Keep as string if all else fails

print("You entered:", user_input)
print("Type:", type(user_input))


'''✅ 1. input("Enter something: ")
This shows a prompt to the user and takes whatever you type as a string.

Example:

python
Copy
Edit
Enter something: 123
Even though it looks like a number, Python sees it as '123' — a string.

✅ 2. try: ... except:
This is a try-except block, used to "try" something that might give an error, and "handle" the error if it happens, so your program doesn't crash.

✅ 3. user_input = int(user_input)
We try to convert the string to an int.
If the user typed something like '42', this will work.

But if they typed 'hello', it would cause an error — because you can’t turn 'hello' into a number.

So if it fails, Python jumps to the next block (except ValueError:).

✅ 4. user_input = float(user_input)
Now we try to convert to a float (a decimal number).

If the user typed 3.14, it will work.
But again, if they typed something like apple, this will fail too.

So if it fails again, we just leave the input as it is (a string).

✅ 5. print("You entered:", user_input)
This just prints the value after trying all the conversions.

✅ 6. print("Type:", type(user_input))
This shows you what Python thinks the type is, using the type() function.

Examples:

'123' becomes int

'3.14' becomes float

'hello' stays as str

✅ 7. pass
In Python, pass means "do nothing." It's like saying "Okay, move on."

We use it here so that if all conversion fails, 
we just let the input stay as it is (a string).'''