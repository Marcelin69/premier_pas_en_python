f = open("monfichier.txt", encoding= "utf-8")
donnees = f.read()
print(donnees)
f.close( )  # fermeture du fi chier
# print ("Le contenu de monfichier.txt est : ")
# # on peut lire le contenu d'un fichier en utilisant la méthode read() ou readlines()
# for ligne in f.readlines( ) :   # lecture des lignes du fichier
#     print (ligne)

# try:                          # utilisation d'une construction try/except pour gérer une exception possible
#     f = open("fichierinexistant.txt")     # tentative d'ouverture d'un fichier qui n'existe pas
#     print ("Contenu du fichier inconnu.")
# finally:                      # code à exécuter quoi que ce soit se passe-t-il que cela arrive
#     if "f" in locals():       # vérification si la variable 'f' existe dans les variables locales
#         f.close( )            # fermeture du fichier s'il a été ouvert avec succès