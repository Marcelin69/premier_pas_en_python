# Récupération des informations de l'utilisateur
nom = input("Quel est votre nom? ")
prenom = input("Quel est votre prénom? ")
age = input("Quel est votre age? ")
rayon = float(input("Quel est le rayon de votr cercle? "))
# Combinaison des noms dans une variable
nom_complet = prenom + " " + nom
# Affichage du nom et prénom de l'utilisateur
print("Bonjour ",nom_complet ," je suis votre assistant virtuel!") 
print("Votre age est"  ,age, "ans")

# calculé l'aire d'un cercle 
pi = 3.14
aire = (pi*rayon)**2
print ("L'aire de votre cercle est de", aire, "cm²")