import requests

Url="http://api.openweathermap.org/data/2.5/weather?appid=0bec186d31de491a34834ff28825e88d&q="
city=input('Enter the city name :')
path= Url + city
json_data=requests.get(path).json()
feu=json_data['weather'][0]['main']
print(json_data)
print(feu)