operateur={"add":"+" ,"multiplication": "*",  "division": "/", "soustraction": "-"}

nbreUserOne = int(input("Entrez premier nombre s'il vous plait : "))
operaUser =  input ("Quel opérateur voulez-vous utiliser ? (add, multiplication, division ou soustraction) ")
nbreUserTwo = int(input("Entrez deuxième nombre s'il vous plait : "))


if(operaUser in operateur):
    if(operateur[operaUser]=="+") :
        resltat = nbreUserOne + nbreUserTwo
    elif(operateur[operaUser] == "*") :
        resltat= nbreUserOne * nbreUserTwo
    elif(operateur[operaUser] == "/") :
        if(nbreUserOne == 0 or  nbreUserTwo == 0):
            print("Impossible de diviser par zéro.")
            resltat =  "Erreur"
        else:
            resltat =  nbreUserOne / nbreUserTwo
    elif(operateur[operaUser] == "-"):
        resltat = nbreUserOne - nbreUserTwo
else:
    print("Vous avez rentré un opérateur incorrect. Merci de bien le saisir.")
    resltat = "Erreur"
print("\n Le résultat est : ",resltat )


# print(nbreUser, operaUser)