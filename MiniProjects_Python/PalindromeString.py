input=input("Enter Palindrome String\n")
pala=input[::-1]
if input == pala :
    print(pala ,"is Palindrom String")
else :
    print("not palindrom string")