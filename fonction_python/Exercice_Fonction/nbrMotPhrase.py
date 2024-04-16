def nombre_mot(phrase):
    mots  = phrase.split()
    
    return len(mots)

retour = nombre_mot("Bonjour à toutes et à tous")

print(retour)