userNbre= int(input("Entrez un nombre svp "))
premier = True
for  i in range (2,userNbre):
    if(userNbre %i==0):
        print (f"{userNbre} n'est pas premier")
        premier = False
        break
if(premier):
    print (f"{userNbre} est un nombre premier")   

    
        
        