amount=float(input('Enter principle amount: '))
rate=float(input("what is interest rate: "))
duration=float(input('time period in Year'))
print(f"{amount+((amount*(rate/100))*duration)}")
