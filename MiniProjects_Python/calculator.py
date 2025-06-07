print('This is a Simple calculator')
num1= float(input('Please enter first number: '))
operator=input('Enter operator i.e + - * / ')
num2=float(input('Please enter second number: '))
if operator == "+" :
    print('Number one + Number two is ',num1+num2)
elif operator == "-" :
    print("Number one - number two = ",num1-num2)
elif operator == "*":
    print("Number one * NUmber two = ",num1*num2)
elif operator == "/" :
    print("Number one/Number two = ", num1/num2)
else :
    print("Uhh, Sorry this is not supportable yet :(")