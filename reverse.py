nbr1 =float(input("Entrez  nombre 1 : "))
nbr2 =float(input("Entrez  nombre 2 : "))
nbr3 =float(input("Entrez  nombre 3 : "))

note = []
note.append(nbr1)
note.append(nbr2)
note.append(nbr3)

print(f"La liste en ordre normale {note}")
note.sort(reverse=True)

print(f"la liste en ordre renversé  est {note}")