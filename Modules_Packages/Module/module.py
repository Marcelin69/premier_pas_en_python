import os

print("le repertoire est :",os.getcwd())#affiche le répertoire courant
print("la liste est :",os.listdir())#affiche la liste des fichiers et dossiers dans le répertoire courant

os.chdir("..")#revenir sur  le dossier parent

print("le repertoire est :",os.getcwd())
print("la liste est :",os.listdir())#affiche les fichiers et dossiers du dossier React
os.mkdir('python/Modules_Packages/Module/modossier')

try:
    os.remove('python/Modules_Packages/Module/fichier.txt') #supprimer un fichier
except FileNotFoundError:
    print("Le fichier n'existe pas.")
try:
    os.removedirs('python/Modules_Packages/Module/modossier') #supprimer un dossier
except FileNotFoundError:
    print("Le dossier n'existe pas.")

path = os.path.join(os.getcwd(), 'Modules_Packages','Module','modossier')

print(path)