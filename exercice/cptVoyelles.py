voyelle = ['a','e','i','o','u','y']

motVerfi = input("Entrez votre mot a compter : ")
motUser = motVerfi.lower()
cpt = 0

for  lettres in voyelle:
    if(lettres in motUser):
        cpt +=1
        print ("Le nombre de",lettres,"dans le mot est :",motUser.count(lettres))
print("Le nombre total des voyelles dans le mot est : ",cpt)

