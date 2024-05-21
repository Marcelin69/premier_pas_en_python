import sqlite3

def barrer(texte):
    return ''.join([u'\u0336{}'.format(c) for c in texte])

class Taches():
    try : 
        def __init__(self):
            self.connection = sqlite3.connect('./Base_de_donnee/challenge/taches.db')
            self.cusseur = self.connection.cursor()
            self.cusseur.execute('''CREATE TABLE IF NOT EXISTS Taches (id INTEGER PRIMARY KEY AUTOINCREMENT, tache TEXT, etat INTEGER) ''')

               
        def ajoutTache(self,tache):
            self.cusseur.execute("INSERT INTO Taches (tache,etat) VALUES (?,?)",(tache,0))
            self.connection.commit()
        
        def afficheTache(self):
            tache = self.cusseur.execute("SELECT * FROM Taches")  
            if tache != None :
                for t in tache:
                  if t[2]:
                       print(f"{t[0]} - {barrer(t[1])}")
                  else :     
                       print(f"{t[0]} - {t[1]}")
                      
                    
        def verifTaches(self,tache):
           taches = self.cusseur.execute("SELECT * FROM Taches WHERE tache = ?",(tache,))
           tache = taches.fetchone()
           if tache :
               return True
           else :
               return False
           
        def termineTache(self,tache):
            if self.verifTaches(tache) :
                self.cusseur.execute("UPDATE Taches SET etat = 1 WHERE tache=?",(tache,))
                self.connection.commit()
            else:
                print("Tache non trouvée")
                
        def suppTaches(self,tache):
            if self.verifTaches(tache) :
                self.cusseur.execute("DELETE FROM Taches WHERE tache=?",(tache,))
                self.connection.commit()
            else:
                print("Tache non trouvée")
                
    except Exception as e:
        print(e)
    finally : 
        def deconnect(self):
            self.connection.close()
    
            
 
    
    


taches = Taches()
# taches.ajoutTache("Aller au supermarché")
# taches.ajoutTache("Appeler Clément")
# taches.ajoutTache("Néttoyer la voiture")
# taches.verifTaches("Appeler Clément")
taches.termineTache('Néttoyer la voiture')
# taches.suppTaches('Appeler Clément')
taches.afficheTache()
