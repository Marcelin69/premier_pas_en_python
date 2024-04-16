nbrUser = int(input("Entrez un nombre s'il vous plais : "))
listPairs =[]
for i in range(nbrUser):
    if(i%2 == 0):
        listPairs.append(i)
        print(f"Le numéro {i} est pair")
    else:
        print(f"Le numéro {i} est impair")
print(listPairs)