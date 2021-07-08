'''
    Sortare topologica a activitatilor pt problema L1_C2
    daca acestea sunt realizabile
    O(n+m)
    folosesc exemplul 2 cel cu REALIZABIL cand nu avem circuit
'''
n=6
m=7
#doar de la a la b
la={1: [2, 5],
    2: [],
    3: [],
    4: [6],
    5: [2, 3, 4],
    6: [3]
    }
viz=[0]*(n+1)
tata=[0]*(n+1)
fin=[0]*(n+1)
ok=0
def DF(x):
    global la, ok, viz, tata, fin
    viz[x]=1
    for y in la[x]:
        if ok!=0:
            break
        if viz[y]==0:
            #print(y, end=" ") #asta e pt parcurgere
            tata[y]=x
            DF(y) ##pana aici parcurgere obisnuita
        elif fin[y]!=1:
                #y nu a fost finalizat este inca in explorare
                print("circuit elementar")
                #afisare lant de la x la y
                v = x
                while v != y:
                    print(v, end=" ")
                    v = tata[v]
                print(y, sep=" ")
                ok=1
    fin[x]=1 #finalizare explorare x

start=1
DF(start)
if ok==0:
    print("REALIZABIL")
    #folosesc var 2 (DF) a sortarii topologice
    #m-am asigurat ca nu exista circuite
    print("Activitatile sortate: ")
    stiva = []
    viz = [0] * (n + 1)

    def DF(x):
        viz[x] = 1
        for y in la[x]:
            if viz[y] == 0:
                DF(y)
        stiva.append(x)  # am terminat de explorat pe x

    # pe componente
    for i in range(1, n + 1):
        if viz[i] == 0:
            DF(i)
    sortate = []
    # sa fie in ordine (nu invers de la coada la cap)
    while len(stiva) > 0:
        u = stiva.pop()
        sortate.append(u)
    print(*sortate)