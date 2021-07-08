'''
    Sortare topologica var 2
    folosind DF

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
stiva=[]
viz=[0]*(n+1)
def DF (x):
    viz[x]=1
    for y in la[x]:
        if viz[y]==0:
            DF(y)
    stiva.append(x) #am terminat de explorat pe x
#pe componente
for i in range(1, n+1):
    if viz[i]==0:
        DF(i)
sortate=[]
#sa fie in ordine (nu invers de la coada la cap)
while len(stiva)>0:
    u=stiva.pop()
    sortate.append(u)
print(*sortate)