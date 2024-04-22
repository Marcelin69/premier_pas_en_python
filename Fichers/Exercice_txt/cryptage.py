with open("Fichers/Exercice/monfic.txt", mode="a",encoding="utf-8") as f:
    f.writelines(["Bonjour ma primiere ligne d'ecritur \n","Vous pensez quoi de mes gests \n"])
    
with open("Fichers/Exercice/monfic.txt", mode="r",encoding="utf-8") as f:
    donnees= f.read().splitlines()
    for  i in donnees:
        cryptage = i[::-1]
        with open("Fichers/Exercice/monfic.txt", mode="a",encoding="utf-8") as f:
            f.writelines(f"{cryptage}\n")
            Decryptage = cryptage[::-1]
            f.writelines(f"{Decryptage}\n")
    
   
    
     