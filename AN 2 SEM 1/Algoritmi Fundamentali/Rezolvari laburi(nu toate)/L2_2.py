'''
     graf neorientat
     graf biconex
     vrea toate componentele biconexe
     folosesc dfs
     2 categorii de muchii
            -> apartin arborelul dfs
            -> muchii de intoarcere (unesc un nod cu un stramos de al sau)
    utilizez o stiva pt memorarea muchiilor
    O(n+m)
'''
n=10
#doar de la a la b si de la b la a
la={1: [10, 5],
    2: [4,8,6],
    3: [5,6,7],
    4: [2,8],
    5: [1,3,6,9,10],
    6: [2,3,5,7],
    7: [3,6],
    8: [2,4],
    9: [5],
    10: [1,5]
    }
stiva=[] #stiva memorare noduri
niv=[0]*(n+1)
niv_min=[0]*(n+1)
nr_componente=0 # nr retele
componentele=[] #subretele
for i in range(n+1):
    componentele.append([])
def DF(x,y):
    global niv, niv_min, nr_componente,siva, la, componentele
    niv[x]=niv_min[x]=niv[y]+1
    stiva.append(x)
    for nod in la[x]:
        if nod==y:
            continue
        else:
            if niv[nod]!=0:
                niv_min[x]=min(niv_min[x], niv[nod])
                continue
            DF(nod,x)
            niv_min[x]=min(niv_min[x], niv_min[nod])

            if niv[x]<= niv_min[nod]:
                nr_componente=nr_componente+1
                k=stiva.pop()
                componentele[nr_componente].append(k)
                while k!=nod:
                    k = stiva.pop()
                    componentele[nr_componente].append(k)

                componentele[nr_componente].append(x)
for i in range(1, n+1):
    if not niv[i]:
        DF(i,1)

print("numarul de componente biconexe: ", nr_componente)
print("componentele sunt:")
for i in range(1, nr_componente+1):
    for nod in componentele[i]:
        print(nod, end=" ")
    print()