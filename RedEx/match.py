import re

while True:
    text = input("Enter your Pass code ")
    user_input = text.lower()
    checking = re.match("hello ", user_input)
    if checking:
        print("Match found\nAccess granted")
        break
    else:
        print("Access not granted, Try again")