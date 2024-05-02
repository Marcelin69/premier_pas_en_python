import random
#tri par selection
nbre = []

def generat_random_list(n,min,max):
    num=random.randint(min,max)
    nbre.append(num)
    if len(nbre)< n:
        generat_random_list(n,min,max)
    return nbre

nombre = generat_random_list(100,-1000,1000)
def selection_sort(l) :
    for non_trie in range(len(l)-1):
        mine = l[non_trie]
        mineIndex =  non_trie
        for i in range(non_trie+1,len(l)) :
            if(l[i]<mine) :
                mine = l[i]
                mineIndex = i
        l[mineIndex] = l[non_trie]
        l[non_trie] = mine
    return l
    
    
print(selection_sort(nombre))
#tri par insertion
