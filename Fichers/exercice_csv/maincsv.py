import csv

with open('Fichers/exercice_csv/titanic.csv') as f:
    lecture = csv.reader(f)
    print(next(lecture,None))
    
with open('Fichers/exercice_csv/ecrit.csv', "w", newline='') as f:
    ecriture = csv.writer(f)
    ecriture.writerow(["prenom","nom","age"])
    ecriture.writerow(["Marcelin3","TINGOUGOUI",22])
    ecriture.writerow(["Kouessi","MARTINI",35])