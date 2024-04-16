nbr1 =float(input("Entrez  nombre 1 : "))
nbr2 =float(input("Entrez  nombre 2 : "))
nbr3 =float(input("Entrez  nombre 3 : "))

note = []
note.append(nbr1)
note.append(nbr2)
note.append(nbr3)
print (max(note)) 
pg = 0
if(nbr1>nbr2 ):
    pg=nbr1
elif(nbr2 > pg and  nbr2 > nbr3):
    pg = nbr2
elif(nbr3 > pg):
    pg = nbr3   
print(pg)