import math


def calculeLaire(rayon) :
    lair = math.pi*rayon**2
    arrondi = round(lair,3)
    print ("Le rayon du cercle est de", rayon, "et le lacet est de", arrondi)
    
calculeLaire(15)