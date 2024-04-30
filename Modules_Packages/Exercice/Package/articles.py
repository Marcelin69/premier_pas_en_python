from Package.utilisateurs import Utilisateur        
        
class Article(Utilisateur):
    def __init__(self,article,utilisateur):
        super().__init__(utilisateur)
        self.article =  article
        
    def ajouterArticle(self,titre,presentation):
        auteur = self.utilisateur
        self.article['Titre']= titre
        self.article['Presentation']= presentation
        self.article['Auteur']= self.utilisateur  
            
    def afficherArticle(self):
        print(">Article")
        print(f"Titre : {self.article["Titre"]}")
        print(f"Presentation : {self.article["Presentation"]}")
        print(f"Auteur : {self.utilisateur["nom"]} {self.utilisateur["prenom"]}")
        # print(self.article[""])