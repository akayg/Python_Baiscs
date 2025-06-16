import re
try :
    string=input("Enter your phone number")
    checking = re.search("[0-9]", string)
    num = checking.group()
    if num.isdigit():
        print(f"{num} number is found")
except Exception :
    print("no number found")