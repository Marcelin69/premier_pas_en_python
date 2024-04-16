
poids = int(input("Entrez votre poids: "))

taille = float(input("Entrez  votre taille : "))

calcImc = poids/taille**2
imc = f"L'IMC d'une personne de {poids} kg et de {taille} m est {calcImc} kg/m^2."

print(imc)