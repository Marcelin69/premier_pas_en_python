nbr1 = int(input("Entrez nobre nombre 1 : "))
nbr2 = int(input("Entrez nobre nombre 2 : "))
nbr3 = int(input("Entrez nobre nombre 3 : "))

note = []
note.append(nbr1)
note.append(nbr2)
note.append(nbr3)
somme=0
for i in note:
    somme  = somme + i
    moyenne = somme / len(note)
print("La somme des notes est :",somme)
print("La moyenne des notes est :",moyenne)
  