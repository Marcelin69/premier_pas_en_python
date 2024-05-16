import requests
import json
import pyttsx3
with open('challenges/Assistance_vocal_meteo/.gitignore') as f:
    lines = f.read()
try:
    meteos = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Île-de-France&appid={lines}")
    vocale = pyttsx3.init()
    content_json = json.loads(meteos.content)
    print(content_json)
    print("\n------------------------------\n")
    meteodesc = content_json["weather"]
    meteohulid = content_json["main"]
    for i in meteodesc:
        desc = i['description']
    temp_c = round(meteohulid['temp']-273.15)
    temp_r = round(meteohulid['feels_like']-273.15)
    region = content_json["name"][0:14]
    humidite = meteohulid['humidity']
    print(f"{region}Température: {temp_c}°C, Ressenti: {temp_r}°C, Humidité: {humidite}%, Description: {desc} \n")
    vocale.say(f"{region}Température: {temp_c}°C, Ressenti: {temp_r}°C, Humidité: {humidite}%, Description: {desc}")
    vocale.runAndWait()
    
except Exception:
    print("Nous avons rencontré un problème.")