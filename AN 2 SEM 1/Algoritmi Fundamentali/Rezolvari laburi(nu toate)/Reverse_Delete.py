'''
    Reverse delete pt gasirea unui APCM
    are la baza DFS
    O(E log V (log log V)^3)
    graf neorientat
'''

def DFS(nod):
    global viz, graf, n
    viz[nod] = 1
    for i in range(n):
        if viz[i]==0 and graf[nod][i]==0:
            DFS(i)
#verific daca un graf este conex
def conex():
    global  graf, n
    viz_conex = [0] * n
    DFS(0) #caut nodurile accesibile din 0

    for i in range(n):
        if viz_conex[i]==0: #nu e accesibil din 0 => graf neconex
            return False
    return True

def RD():
    global viz, graf, n, muchii, arbore, cost
    muchii=sorted(muchii,  key=lambda a: a[2]) #sortare muchii crescator dupa cost


    for (u,v,w) in muchii:
        # sterg muchia din graf:
        graf[u][v]=graf[v][u]=0

        if conex() == False:
            #daca nu mai e conex o pun la loc
            graf[u][v] = graf[v][u] = w
            arbore.append((u,v))
            cost += w
            if len(arbore)==n-1: #un arbore are n-1 muchii
                break
#lucrez de la 0 ca imi e mai usor
muchii=[(0,1,28), (1,2,16), (1,6,14), (2,3,12), (3,6,18),
        (3,4,22), (4,6,24), (4,5,25), (5,0,10)]
n=7 #noduri
graf=[
    [0, 28, 0, 0, 0, 10, 0],
    [28, 0, 16, 0, 0, 0, 14],
    [0,16,0,12,0,0,0],
    [0,0,12,0,22,0,18],
    [0,0,0,22,0,25,24],
    [10,0,0,0,25,0,0],
    [0,14,0,18,24,0,0]
]
cost=0
arbore=[]
viz=[0]*n
RD()
print("muchiile APCM sunt: ", *arbore)
print("costul arborelui este: ", cost)