
action = input("Entrez une action a réaliser (+:Ajouter, -:Terminer, s:Supprimer, a:Afficher, q:Quitter): ")

class Taches():
    def __init__(self,taches):
        self.taches = taches
    
    def afficher_tache(self):
        self.taches
        print('🤞🤞🤞🤞🤞🤞🤞🤞')
        for x,y in enumerate(self.taches):
            print(f" {x} : {y} - {self.taches[y]}")
    
    def ajout_tache(self,nom_tache,statut):
        self.taches[nom_tache] = statut
        
    def  supprimer_tache(self,tacheid):
        if tacheid == "" :
          print("veuillez entrez un nombre")
        else:
            if(tacheid>len(self.taches)) or (tacheid<0):
                 print("Erreur de numéro de tâche.")
            else :
                for x,y in enumerate(self.taches):
                    if(x == tacheid):
                        self.taches.pop(y)
                        print("La tâche  a été supprimée.")
                        break
    def  modifier_tache(self,tacheid):
        if tacheid == "" :
          print("veuillez entrez un nombre")
        else:
            if(tacheid>len(self.taches)) or (tacheid<0):
                print("Erreur de numéro de tâche.")
            else :
                for x,y in enumerate(self.taches):
                    if(x == tacheid):
                        self.taches[y]= True
                        print("La tache est maintenant terminée.")
                        break
       
        
tache = Taches({})
while action !=  "q":
    if action == "+":
        nom_tache = input("Entrez le nom de la tâche s'il vous plaît : ")
        tache.ajout_tache(nom_tache,False)
    elif action == "a":
        tache.afficher_tache()
    elif action == "s":
        tache.afficher_tache()
        tacheid = input("Entrez le numéro de la tâche à supprimer : ")
        if type(tacheid) != "Int" :
            print("Veuillez entrer un nombre.")
        else:
             tache.supprimer_tache(int(tacheid))
    elif  action == "-":
        tache.afficher_tache()
        tacheid = input("Entrez le numéro de la tache terminé : ")
        if type(tacheid) != "Int" :
            print("Veuillez entrer un nombre.")
        else:
            tache.modifier_tache(int(tacheid))
    else:
        print ("Veuillez choisir une option valide")
    action = input("Entrez une action a réaliser (+:Ajouter, -:Terminer, s:Supprimer, a:Afficher, q:Quitter): ")