class NegativeNumberError(Exception):
    pass

def check_positive(no):
    if no<0:
        raise NegativeNumberError("Number should be +ve")
    else : print('no is +ve')


try :
    n=int(input('enter number'))
    check_positive(n)

except NegativeNumberError as ne :
    print(f'custome error: {ne}')
