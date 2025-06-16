import requests

name = input("Enter your name: ")
url=f"https://api.agify.io?name={name}"
response=requests.get(url)

if response.status_code==200:
    data=response.json()
    print(f"Name :{data['name']} Predicted age is {data['age']}")

else:
    print("Some error occured,",response.status_code)