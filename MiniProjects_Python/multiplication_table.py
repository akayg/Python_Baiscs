# Prompt the user to enter a number for which the multiplication table will be generated
multipleof = int(input('Enter a number '))

# Loop through numbers 1 to 10
for i in range(1, 11):
    # Print the multiplication result in the format "number x i = result"
    print(f"{multipleof}x{i}={i*multipleof}")