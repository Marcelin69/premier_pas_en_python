import  math
# recupération des données
angle_deg = float(input("Entrez votre  angle en degrés : "))
angle_rad = float(input("Entrez votre angle en radians : "))


angle_radiant = (math.pi/180) * angle_deg # conversion de l'angle en radian

angle_degre =  (180 * angle_radiant)/ math.pi  # conversion de l'angle en degree

# affichage du resultat de  la conversion
print("Angle en radians : ", angle_radiant)

print ("Angle en degré est ", angle_degre)
