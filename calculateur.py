argent = int(input("Entrez votre argent: "))
prix_Produit = float(input("Entrez le prix du produit "))
quantité_Produit= int(input("Entrez la quantique du produit "))


prix_total = prix_Produit*quantité_Produit
monnaie = argent - prix_total

print("Le reste de votre argent est : ", monnaie ,  " euros")  