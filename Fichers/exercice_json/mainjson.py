import json

data=('{"nom": "Dupont", "age": 32, "ville": "Paris","inFrance":true}')
donnes = json.loads(data)
print(donnes)
print("Nom : ", donnes["nom"])
print("age : ", donnes["age"])

with open("Fichers/exercice_json/data.json") as f:
    donnees = json.load(f)
    print(donnees)
    
diction = {"nom": "Dupont", "age": 32, "ville": "Paris","inFrance":True}

dictionnaire = json.dumps(diction) #convertit un dictionnaire en chaine de caractère JSON
print(dictionnaire)

#On peut également ajouter des éléments au dictionnaire ou le modifier
diction["nouveauChamp"]="Monde"
dictionnaireModifie = json.dumps(diction)
print(dictionnaireModifie)

#on peut aussi supprimer un champ du dictionnaire
del diction["age"]
dictionnaireSupprime = json.dumps(diction)
print(dictionnaireSupprime)

# ecriture dans un fichier json
with open("Fichers/exercice_json/dictconv.json","w") as f :
    json.dump(diction, f)
