class AgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeError(f"Age must be 18 or above. your age is {inn}")
try:
    inn = int(input("Please enter your age"))
    check_age(inn)
except AgeError as e:
    print(e)
