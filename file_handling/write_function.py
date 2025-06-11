try:
    name =input('Enter your name: ')
    age =input('enter your age: ')
    with open('file_handling/userdata.txt',"w") as f: 
        f.write(f'username :{name} and age {age}')

except Exception as e:
    print (f"something went wrong {e}")