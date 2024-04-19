action = input("Entrez une action a réaliser (+: Ajouter, s: Supprimer, t: Afficher le prix total, a: Afficher, m: Modifier q: Quitter): ").lower()

class Achats():
    def __init__(self,achats,quantite):
        self.achats = achats
        self.quantite = quantite
    
    def ajouter_achat(self,produit,prix,quantite):
        """Ajoute un nouvel achat à la liste des achats"""
        if(produit in self.achats): # On vérifie si le produit est déjà dans la liste d'achats     
            print("Erreur : le produit existe déjà dans votre panier.🫨\nsolution : Vous voulez le modifier si OUI sélectionnez l'action m.😁")        
        else :# Sinon on l'ajoute avec son prix et sa quantité
            self.achats[produit] = prix
            self.quantite.append(quantite)
            
    def modifier_produi(self,produit,prix,quantite):
        """modifier un produit à la liste des achats"""
        try:
            index = list(self.achats.keys()).index(produit)
            self.achats[produit] = prix
            self.quantite[index] = quantite 
            print("Votre produit est modifié.🎉") 
        except ValueError:
            print("Le produit n'est pas dans votre panier.🤷‍♂️")     

    def afficher_panier(self):
        """Retourne le contenu du panier d'achats"""
        print('🤞🤞🤞🤞🤞🤞🤞🤞')
        if(len(self.achats)==0):
            print("Votre panier est vide.😒")
        else:
            for x,y in enumerate(self.achats):
                print(f" {x} : {y} - {self.achats[y]} € Quantité : {self.quantite[x]}")
        
    def prix_totale(self):
        """Calcule et retourne le montant total de l'achat (somme des produits * leur prix)"""
        somme = 0
        for x,y in enumerate(self.achats):
            somme += self.achats[y]*self.quantite[x]
        print(f"Prix total : {somme} €")
        
    def  supprimer_un_produit(self,achatsId):
        """Supprime un produit du panier d'achats"""
        try:
            index = list(self.achats.keys()).index(achatsId)
            del self.achats[achatsId]
            del self.quantite[index]
            print("Produit supprimé !🤗 ")
        except ValueError:
            print("Le produit n'est pas dans votre panier.😒")
        
        
achats = Achats({},[])

while action != "q":
    if action  == '+':
        produit = input("Entrez le nom du produit : ")
        quantite = int(input("Combien voulez-vous ajouter ? : "))
        prix = float(input("Quel est le prix de ce produit (en €) ? : "))
        if(type(quantite) is not int or type(prix) is not float or type(produit)!=str):
            print("Erreur de saisie.")
        else:
            achats.ajouter_achat(produit,prix,quantite)
    elif action == "s":
        achatsId = input("Entrez le produit a suprimmé : ")
        if(type(achatsId)!=str):
            print("Erreur de saisie.")
        else:
            achats.supprimer_un_produit(achatsId)
    elif action == "m":
        achatsId = input("Entrez le produit a modifié : ")
        quantite = int(input("Combien voulez-vous ajouter ? : "))
        prix = float(input("Quel est le prix de ce produit (en €) ? : "))
        if(type(quantite) is str or type(prix) is str  or type(achatsId)!=str):
            print("Erreur de saisie.")
        else:
             achats.modifier_produi(achatsId,prix,quantite)
    elif action == 'a':
        achats.afficher_panier()
    elif action == "t":
        achats.prix_totale()
    else:
        print("Action inconnue.")
    action = input("Entrez une action a réaliser (+: Ajouter, s: Supprimer, t: Afficher le prix total, a: Afficher, m:Modifier, q: Quitter): ").lower()
    
    
    
    
    #   mail=input('Entrer votre adresse e-mail pour recevoir vos commandes par email : ')
    #     with smtplib.SMTP_SSL('smtp.gmail.com',  465) as server:
    #         server.login('votreaddressemail@gmail.com','votrpassword') # Remplacer par votre addresse email et mot de passe gmail
    #         #server.login(email_user, password)
    #         text = f"Voici votre commande : \n\n{achats