id=input('Please Enter Id')
pasw=input('Please enter Password')


while id != 'admin' or pasw != '12345':
    print('Wrong ID or password. Please try again.')
    id = input('Please Enter Id: ')
    pasw = input('Please enter Password: ')
    if id == 'admin' and pasw == '12345':
        print('Logged in Thank you!')
        break