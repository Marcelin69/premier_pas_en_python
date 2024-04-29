import math

def perimetre(rayon):
    if (type(rayon) != int and type(rayon) != float) :
        raise TypeError("le type de rayon doit être un nombre réel")
    if rayon<0:
       raise ValueError("le rayon doit être positif")
    return  2 *math.pi*rayon
