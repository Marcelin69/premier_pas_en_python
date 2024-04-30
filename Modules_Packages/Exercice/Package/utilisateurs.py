class Utilisateur():
    def __init__(self,utilisateur):
        self.utilisateur =  utilisateur
       
    def ajouter(self,nom,prenom,age):
        """Ajoute un nouvel utilisateur"""
        self.utilisateur["nom"]=nom
        self.utilisateur["prenom"]=prenom
        self.utilisateur["age"]=age
        print(f"{nom} {prenom}, est ajouter")
    
          
    def info(self):
        print(self.utilisateur["nom"])
        
