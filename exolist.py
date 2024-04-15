import random

motxChoix = ["pierre", "feuille", "ciseaux"]  # Les choix de mot sont dans une liste.
compteurMot = 0   # Compteur pour savoir si c'est le tour du joueur ou de l'ordinateur.
ordiMot = random.choice(motxChoix)    # Mot aléatoire pour l'ordinateur.



userMot = input("Sélectionné pierre, feuille ou ciseaux : ")
if userMot in  motxChoix:
    if userMot ==  ordiMot:
        print("Egalité")
    else:
        if(userMot== "pierre"  and ordiMot=="feuille")\
        or(userMot == "ciseaux" and ordiMot == "pierre")\
        or(userMot == "feuille" and ordiMot ==  "ciseaux"):
            print("Vous avez perdu. ")
        else : 
            print("Vous avez gagné.")
    print(f"Le choix de l'ordinateur est {ordiMot}")
else : 
    print("Les options disponibles sont pierrées, feuille et ciseaux.")

  
