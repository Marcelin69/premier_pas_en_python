import json

with open("Projets/nuage_de_mot/fichier.txt", "w", encoding="utf-8", newline="") as f:
    f.write("Python est un langage de programmation puissant et facile à apprendre. Il dispose de structures de données de haut niveau et permet une approche simple mais efficace de la programmation orientée objet. Parce que sa syntaxe est élégante, que son typage est dynamique et qu'il est interprété, Python est un langage idéal pour l'écriture de scripts et le développement rapide d'applications dans de nombreux domaines et sur la plupart des plateformes.L'interpréteur Python et sa vaste bibliothèque standard sont disponibles librement, sous forme de sources ou de binaires, pour toutes les plateformes majeures depuis le site Internet https://www.python.org/ et peuvent être librement redistribués. Ce même site distribue et pointe vers des modules, des programmes et des outils tiers. Enfin, il constitue une source de documentation.L'interpréteur Python peut être facilement étendu par de nouvelles fonctions et types de données implémentés en C ou C++ (ou tout autre langage appelable depuis le C). Python est également adapté comme langage d'extension pour personnaliser des applications.Dans ce tutoriel, nous introduisons, de façon informelle, les concepts de base ainsi que les fonctionnalités du langage Python et de son écosystème. Il est utile de disposer d'un interpréteur Python à portée de main pour mettre en pratique les notions abordées. Si ce n'est pas possible, pas de souci, les exemples sont inclus et le tutoriel est adapté à une lecture.Pour une description des objets et modules de la bibliothèque standard, reportez-vous à La bibliothèque standard. La référence du langage Python présente le langage de manière plus formelle. Pour écrire des extensions en C ou en C++, lisez Extension et intégration de l'interpréteur Python et Manuel de référence de l'API Python/C. Des livres sont également disponibles qui couvrent Python dans le détail.L'ambition de ce tutoriel n'est pas d'être exhaustif et de couvrir chaque fonctionnalité, ni même toutes les fonctionnalités les plus utilisées. Il vise, en revanche, à introduire les fonctionnalités les plus notables et à vous donner une bonne idée de la saveur et du style du langage. Après l'avoir lu, vous serez capable de lire et d'écrire des modules et des programmes Python et vous serez prêt à en apprendre davantage sur les modules de la bibliothèque Python décrits dans La bibliothèque standard..")
with open("Projets/nuage_de_mot/fichier.txt", "r", encoding="utf-8", newline="") as f:
     # Lecture du contenu complet de fichier.txt et stockage dans la variable texte
    texte = f.read()
    # print(texte)
    modifi = texte.lower()
    listeText = modifi.split()  # On transforme le  texte en une liste de caractères
    motu = "Python"
    data={}
    for mot in  listeText:   # Pour chaque élément (mot) de la liste des mots :
        if(mot in modifi) :
            if(len(mot)>4): 
                data[mot] = modifi.count(mot)
            
    ordonData = sorted(data.items(), key=lambda item : -item[1]) # Tri par nombre d'apparition décroissant
    recoerd = dict(ordonData)
   
with open("Projets/nuage_de_mot/nuage_mot.json", "w",encoding="utf-8") as  j:
    datajson = json.dumps(recoerd, ensure_ascii=False)
    j.writelines(datajson)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        # mot.count(listeText)
        # for motreche in listeText:
        #     if(motreche in mot) :
        #         print (motreche,":",motreche.count(mot))
            
        