'''
    Sortare topologica var 1
    folosind BF si o lista cu gradele interne ale nodurilor
    incep de la nodurile cu gradul intern 0
    graf orientat
    nu merge pe graf cu circuite
'''
n=6
m=7
#doar de la a la b
la={1: [2, 5],
    2: [],
    3: [], # am scos muchia (3,5) ca sa nu mai fie circuit
    4: [6],
    5: [2, 4],
    6: [3]
    }
#calculez gradul intern pt fiecare varf
#de cate ori apare un nod in liste
grad_intern=[0]*(n+1)
for i in range(1, n+1):
    for key in la.keys():
        for nod in la[key]:
            if i==nod:
                grad_intern[i]=grad_intern[i]+1

    #alg de sortare topologica
sortate=[]
from collections import deque
c=deque([])
#adaug in coada nodurule care au gradul 0
for i in range (1,n+1):
    if grad_intern[i]==0:
        c.append(i)
nod=0
while len(c)>0:
    i=c.popleft()
    sortate.append(i)
    for j in la[i]: #pt fiecare muchie de la i la j
        nod=j
        grad_intern[j]=grad_intern[j]-1 #scad gradul
        if grad_intern[j]==0: #daca e 0 il adaug in coada si pe el
            c.append(j)
#detectare nod in care incepe si se termina un circuit
#nodul la care se blocheaza
if len(sortate)!=n:
    print ("graf cu circuit \nnodul la care avem circuit: ", nod)
else:
    print(*sortate)