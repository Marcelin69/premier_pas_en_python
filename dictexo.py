uniteValid =  {"km": 0.001,"cm" : 100, "mm":1000}

userValeur = int(input("Entrez une distance en (m) : "))

userUnite = input("Entrez l'unité (km, cm ou mm)")
unitecovert = userUnite.lower()  #pour eviter les majuscules et les minuscules
if(unitecovert in uniteValid):
        result = userValeur*uniteValid[unitecovert]
        print(f"Conversion : {userValeur} m en {unitecovert} = {result} {unitecovert}")        
else:
    print(f"L'unité {userUnite} est invalide")
    