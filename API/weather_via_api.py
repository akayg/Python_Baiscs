import toml 
import requests
#load toml file for openweatherAPI 
config = toml.load("API/api_key.toml")

# Access api key
api_key = config["api_open"]
city=input("Enter city ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code==200:
    data=response.json()
    # print(data)
    print(f"Current Temprature of {data['name']} is {data['main']['temp']} ") 

else: 
    print("Some error occured,",response.status_code)