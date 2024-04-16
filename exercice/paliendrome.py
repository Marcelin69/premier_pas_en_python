userChaine = input("Entrez une mote s'il vous plait : ")
var_chaine = userChaine.lower().replace(" ","")
listCreat = []
for i in var_chaine:
    listCreat.append(i)
listCreat.reverse()
chaine = ''.join(listCreat)
motplien = chaine.replace(' ', '')

if(motplien == var_chaine):
    print(f"\"{userChaine}\" est un palindrome")
else:
    print(f"\"{userChaine}\" n'est pas un palindrome")
