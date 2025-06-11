try:
    a = int(input('Number 1'))
    b = int(input('Number 2'))
    result = a / b
    print(result)

except ZeroDivisionError:
    print("cant divide by zero")

except ValueError:
    print("Enter numbers only")