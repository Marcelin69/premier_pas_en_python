text = "bonjour toto"

text2 = "Un  cahsseur sachant cahsser sait chasser sans son chien"

def reverse_string(str):
    
    revers = str.split()
    print(revers)
    
    print(str[::-1])
    
def shotword(word):
    mots = word.split(" ")
    cout = ""
    long = ""
    for mot in mots:
        if(len(mot)>=len(long)):
            cout = long
            long = mot
        elif (len(mot)< len(cout)):
            cout = mot
    print(long,cout)
     
reverse_string(text) # Output: "ototnirbo"
shotword(text2)
    
    
    
    
def max_min(word):
    mots = word.split()
    mots.sort()
    mine = min(mots,key=len)
    maxe = max(mots,key=len)
    
    return(mine,maxe)

# ordre alphabetique
def get_max_min(word):
    mots = word.split()
    mine,maxe = max_min(word)
    
    allmin_word = [w for w in mots if len(w)==len(mine) ]
    allmax_word = [w for w in mots if len(w)==len(maxe) ]
    
    allmin_word.sort()
    allmax_word.sort()
    
    
    return(allmin_word[0],allmax_word[0])
        

# mine,maxe=get_max_min(text2)
mine,maxe=max_min(text2)

print("le mot le plus petit est", mine)
print("le mot le plus grand est", maxe)