# nomComplet =  "Marcelin TINGOUGOUI"
nomComplet =  "marcelin kouessi"
age = 59

nom = nomComplet.split(" ")[1]
prenom = nomComplet.split(" ")[0]
inde1= nom[0].upper()
inde2= prenom[0].upper()

affichage= f"l'initiale du {nom} {prenom} est : {inde1}{inde2}"
print(affichage)
presnetation = ("Bonjour je m'appelle "+ prenom + " " + nom + ", j'ai " + str(age) + " ans")
presentation = f"Bonjour je m'appelle {prenom}, j'ai {age} ans"
print (presentation)

