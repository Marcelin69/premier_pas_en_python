try:
    with open("Gestion_erreur/except_emessage/fichie.txt") as f : 
        text = f.read()
        print(text)
        volume = float(text)
except Exception as e:
    print(e)
finally:
    print("fin de code")