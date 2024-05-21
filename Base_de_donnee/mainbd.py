import sqlite3

connection = sqlite3.connect('./Base_de_donnee/celebrites.db')
print('connecté')
curseur = connection.cursor()
try:
    curseur.execute('''CREATE TABLE IF NOT EXISTS  celebrites (id INTEGER PRIMARY KEY AUTOINCREMENT,nom TEXT,prenom TEXT,age INTEGER,popularites REAL)''')
    
    curseur.execute('''INSERT INTO celebrites(nom,prenom,age,popularites) VALUES ("Tingougoui","marcelin",23,8.5)''')
    curseur.execute('''INSERT INTO celebrites(nom,prenom,age,popularites) VALUES ("KOUESSI","Avivi",33,9.5)''')
    curseur.execute('''INSERT INTO celebrites(nom,prenom,age,popularites) VALUES ("DAHOUE","Jonas",50,5.5)''')
    curseur.execute('''INSERT INTO celebrites(nom,prenom,age,popularites) VALUES ("LOKOSSOU","Nicole",18,7.5)''')
    connection.commit()
    valeur = curseur.execute('''SELECT nom FROM celebrites WHERE celebrites.id == 2''')
    
    # curseur.execute('''UPDATE celebrites SET nom = 'KOHOUE' WHERE celebrites.id == 2''')
    # valeur = curseur.execute('''SELECT nom FROM celebrites WHERE celebrites.id == 2''')
    
    # curseur.execute('''DELETE FROM celebrites WHERE celebrites.id == 2''')
    # connection.commit()
    # valeur = curseur.execute('''SELECT * FROM celebrites ORDER BY id DESC''')
    
    for i in valeur:
        print(i)
        # for y in i:
        #     print(y)
except Exception as e:
    print(e)
finally:(
connection.close()
)