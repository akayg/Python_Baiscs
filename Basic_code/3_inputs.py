# a = input("enter some num here")
# b = input("enter some other number")
# sum = a+b
# print(sum)
# by default above program will return 1+2=12 bcz it will take 
# both number as string for eg a+b=ab

# define datatype
# a:int
# b:int type1 for defining
a = int(input('enter number : ')) #second way to define it
b = int(input("enter second number : ")) 
'''Even though you said a: int, you're assigning a string to it because input() always returns a string.

So Python doesn’t stop you — it'll happily say:

"Okay, a is supposed to be an int... but you gave me a string? Sure, whatever."'''
sum=a+b
print(sum) #or can directly print a+b

