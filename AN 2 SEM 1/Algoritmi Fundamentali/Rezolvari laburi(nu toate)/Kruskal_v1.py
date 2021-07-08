'''
    Determinare APCM folosind colorarea componentelor
    r[u]= culoarea compnentei din care varful u face parte
    graf neorientat
    lucrez pe lista de muchii (x, y, cost)
    O(m log n + n^2)
'''
def reuneste(u,v):
    global r,n
    r1=r[u] #culoarea nodului u
    r2=r[v] #culoarea nodului v
    for k in range (1,n+1):
        if r[k]==r2: #coloram restul componentelor
            r[k]=r1
muchii=[(1,2,28), (2,3,16), (2,7,14), (3,4,12), (4,7,18),
        (4,5,22), (5,7,24), (5,6,25), (6,1,10)]
n=7 #noduri
#sortez crescator dupa cost
muchii=sorted(muchii, key=( lambda t: t[2]))

#initializez
r=[0] #'colorez' componentele
for i in range(1,n+1):
    r.append(i)
nrmsel=0
cost=0
print("Muchiile arborelui sunt: ")
for m in muchii:
    if r[m[0]] != r[m[1]]: #daca nu fac parte din ac componenta (adica nu avem ciclu)
        #printez muchiile
        print(m[0], m[1])
        reuneste(m[0], m[1])
        cost=cost+m[2]
        nrmsel=nrmsel+1
        if nrmsel==n-1: #ca sa fie arbore trebuie sa aiba n-1 muchii
            break;
print("Costul este: ", cost)
print("vectorul de reprezentanti: ", r[1:])