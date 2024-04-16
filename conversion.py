
choixUser = input("Entrez votre choix de conversion Fahrenheit ou Celsius : ")

temperature= float(input("Entrer la température à convertir : "))
choixVerif = choixUser.lower()
fehrenheit = (temperature - 32) * 5/9
celsius = (temperature -32)/1.9

if(choixVerif =="fahrenheit"):
    arrondi = round(celsius,2)
    print ("La temperature en Celsius est : ", arrondi,"°C")
elif(choixVerif == "celsius"):
    arrondi = round(fehrenheit,2)
    print ("La temperature en Fahrenheit est : ", arrondi,"°F")
else:
    print ("Vous n'avez pas entré une option valide, veuillez recommencer.")