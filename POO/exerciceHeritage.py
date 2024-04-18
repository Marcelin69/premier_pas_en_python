class Personne():
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age  = age
        
    def affiche_info(self):
        print (f"Info : {self.nom} {self.prenom}, Age: {self.age} ans")
        
class Etudiant(Personne):
    def  __init__(self,nom,prenom,age,notes):
        super().__init__(nom,prenom,age)
        self.notes = notes
        
    def affiche_note(self):
        print("Notes : ",self.notes)
    
    def ajouter_note(self,matier,note):
        self.notes[matier] = note
    
    def calculeMoyen(self):
        somme=0
        for i in self.notes : 
            somme += self.notes[i]
        moyenne = somme/len(self.notes)
        print(f"la moyenne de {self.nom} {self.prenom} est de {moyenne}")


romeo = Personne("TINGOUGOUI","Marcelin", 23)
alice = Etudiant("KOUESSI","Alice",25,{"Math":10,"Français":12, "Anglais":19})

# romeo.affiche_info()
# alice.ajouter_note("Science",7)
# alice.affiche_note()
alice.calculeMoyen()
