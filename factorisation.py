userNbre = int(input("Entre le nombre à factoriser s'il vous plair : "))
factoriel = 1
if(userNbre == 0):
    print(1)
else:
    for i in range(userNbre):
        decon = (userNbre - i)
        factoriel *=  decon 
print(f"la factorielle de {userNbre} est : {factoriel}")
        
    