
uniterDeMesure = {"km":0.001 , "hm": 0.01, "dam":0.1 , "m" :1 , "dm":10 , "cm":100 ,  "mm":1000}
userMesur = float(input("Entrez votre distance en mètre (m) : "))
userUniter = input("Entrez votre unité de conversion s'il vous plaît : ")

def convertisseur(mesur,uniterverif,unitedef):
    
    if(uniterverif in unitedef):
            resultat =(f"La conversion de {mesur} m en {uniterverif} est {mesur * uniterDeMesure[uniterverif]} {uniterverif}")
            return resultat
    else:
            return  "Erreur d'unités ! Vous avez saisi une ou plusieurs unités incorrecte."
         
    
print(convertisseur(userMesur,userUniter,uniterDeMesure))