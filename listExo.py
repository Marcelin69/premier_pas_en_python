temperature = [23,22,19,26,24,28,26]
moyenne = 0
for moy in temperature:
     moyenne += moy
     nombre_mesure = len(temperature)
moyenne /= nombre_mesure
degr = round(moyenne,2) # conversion Fahrenheit
print(f"la temperature moyenne est {degr} °C")


villes = ["Paris", "Strasbourg", "Marseille", "Bordeaux"]
numeros = [75, 67, 13, 33]

for i, v in enumerate(villes):
   print(v,numeros[i])
   