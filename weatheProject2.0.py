import requests, json, os, csv
import pandas as pad
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("apiKey")
EMAIL_ADOR = os.getenv("EMAIL_ADOR")
PASSWORD = os.getenv("PASSWORD")

lat = input('lat: ')
log = input('log: ')
#cityname = input('cityname: ')
#resCity = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apiKey}", timeout=10)

res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={log}&appid={apiKey}", timeout=10)
ress = res.json()['main']

with open("c:/Users/liliz/OneDrive\Documenti\python/WeatherAPIKey/weather.csv", "r+", newline="") as f:
    # Create a CSV writer using the field/column names
    writer = csv.DictWriter(f, fieldnames=ress)
    writer.writeheader()
    writer.writerow(ress)

poke = pad.read_csv("c:/Users/liliz/OneDrive\Documenti\python/Weather/weather.csv")
print(poke)