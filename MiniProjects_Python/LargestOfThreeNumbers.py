n1=int(input('Enter three numbers: \n'))
n2=int(input('\n'))
n3=int(input('\n'))

if n1<n2 and n2 >n3:
    print(n2,'is largest number')
elif n1>n2 and n3<n2:
    print(n1,'is Largest number')
else :
    print(n3,'is Largest number')