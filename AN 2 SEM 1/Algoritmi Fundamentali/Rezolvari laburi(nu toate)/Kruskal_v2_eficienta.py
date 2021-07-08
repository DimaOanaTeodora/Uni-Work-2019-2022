'''
    Det APCM folosind arbori Union/Find
    graf neorientat
    lucrez pe lista de muchii (x, y, cost)
    O(m log n)
    implementare cu paduri disjuncte
'''
def reprez(u):
    #determinare radacina arbore care contine u
    global tata
    '''
    while tata[u] !=0:
        u=tata[u]
    return u
    '''
     #optimizare
    if tata[u] ==0:
        return u
    tata[u]=reprez(tata[u])
    return tata[u]


def reuneste(u,v):
    #reuniune ponderata
    global tata,h
    ru=reprez(u)
    rv=reprez(v)
    '''
    if h[ru] < h[rv]:
        tata[ru] = rv
    elif h[ru] > h[rv]:
        tata[rv] = ru
    else:
        tata[rv] = ru
        h[ru] += 1
    '''
    if h[ru]>h[rv]:
        tata[rv]=ru
    else:
        tata[ru]=rv
        if h[ru]==h[rv]:
            h[rv]=h[rv]+1

#lista de muchii (x, y, cost)
muchii=[(1,2,28), (2,3,16), (2,7,14), (3,4,12), (4,7,18),
        (4,5,22), (5,7,24), (5,6,25), (6,1,10)]
n=7 #noduri

#initializare
tata=[0]*(n+1)
h=[0]*(n+1)

#sortez crescator dupa cost
muchii=sorted(muchii, key=( lambda t: t[2]))

nrmsel=0 #nr muchii selectate (arbore -> n-1 muchii)
cost=0
print("Muchiile arborelui sunt: ")
for m in muchii:
   if reprez(m[0]) != reprez(m[1]): #daca nu fac parte din ac componenta (adica nu avem ciclu)
        #printez muchiile
        print(m[0], m[1])
        reuneste(m[0], m[1])
        cost=cost+m[2]
        nrmsel=nrmsel+1
        if nrmsel == n - 1:  # ca sa fie arbore trebuie sa aiba n-1 muchii
            break

print("Costul este: ", cost)
print("Arborele de paduri disjuncte: ", tata[1:])
print("Vectorul de inaltimi: ", h[1:])