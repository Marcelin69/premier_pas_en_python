import requests


stationNaza = requests.get("http://api.open-notify.org/astros.json")

if(stationNaza.status_code == 200):
    dataNaza = stationNaza.json()
    message = dataNaza["message"]
    nombre = dataNaza["number"]
    print(f"Le message est un", message)
    print(f"les personnes qui sont dans le verceau sont au nombre de",nombre)
    for info in dataNaza["people"]:
        print(info["name"], "est dans le verseau", info["craft"])
else:
    print("Failed to get data from server.")