def main():
    print("Hello, User!")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"The sum of {a} and {b} is {a + b}")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()