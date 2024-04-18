class Rectangle:
    def __init__(self,longeur,largeur):
        self.longeur = longeur
        self.largeur = largeur
    
    def perimetre(self):
        perimet = (self.longeur + self.largeur)*2
        return perimet
    
    def aire(self):
        aire =  self.longeur * self.largeur
        return aire
    
    def est_carre(self):
        if(self.longeur == self.largeur):
            return True
        else :
            return False

rect = Rectangle(5,5)

perimetre = rect.perimetre()
aire = rect.aire()
verif = rect.est_carre()

print(f"Périmetre : {perimetre} m ")
print(f"Aire : {aire} m²")
print("Est-ce un carré ?", verif)