import random

devinet = random.randint(0,10)
userDvin = int(input("Entrez un nombre entre  0 et 10: "))

cpt = 1
while devinet != userDvin:
    if cpt ==3:
        print(f"Perdu ! le nombre a déviné est {devinet}")
        break
    else:
        if(userDvin < devinet):
            print("Votre nombre est trop petit.")
            cpt += 1
            userDvin = int(input("Entrez un nombre entre  0 et 10: "))    
        elif(userDvin>devinet):
          print("Votre nombre est trop grand.")
          cpt += 1
          userDvin = int(input("Entrez un nombre entre  0 et 10: "))     
if(userDvin==devinet):
    print("Félicitations vous avez trouvé le bon nombre en", cpt,"essais.")
    