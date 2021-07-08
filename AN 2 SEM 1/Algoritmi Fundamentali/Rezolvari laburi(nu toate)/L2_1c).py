'''
     graf neorientat
     graf biconex
     vrea componenta biconexa maximala (cu cele mai multe noduri)
     folosesc dfs
     2 categorii de muchii
            -> apartin arborelul dfs
            -> muchii de intoarcere (unesc un nod cu un stramos de al sau)
    utilizez o stiva pt memorarea muchiilor
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
maxim=0
componenta_max=[]
muchii=[]
def DF(x,y):
    global niv, niv_min, nr_componente,siva, la, componentele, maxim, componenta_max, muchii
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
                if maxim< len(componentele[nr_componente]):
                    maxim = len(componentele[nr_componente])
                    componenta_max=componentele[nr_componente]

for i in range(1, n+1):
    if not niv[i]:
        DF(i,1)

print("nodurile din componenta maxima sunt:", *componenta_max)
print("muchiile care o formeaza sunt: ")
for i in range(len(componenta_max)-1):
    for j in range(i+1, len(componenta_max)):
        if componenta_max[i] in la[componenta_max[j]]:
            print( componenta_max[i], componenta_max[j], sep=" ")
'