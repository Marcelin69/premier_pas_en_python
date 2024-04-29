try:
    with open("Gestion_erreur/exectionmessage/fichier.txt") as f : 
        text = f.read()
        print(text)
except Exception:
    print("Le code a  rencontré une erreur.")

print("fin de code")