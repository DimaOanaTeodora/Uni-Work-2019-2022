'''
    Acelasi Dijkstra intre s si t
    complicata cu 2^-p
    vrea drum MAXIM dar fiind subunitara de aplica Dijkstra
'''
graf = {
    1: {2: 10, 3: 5},
    2: {4: 1},
    3: {2: 3, 4: 9, 5: 2},
    4: {},
    5: {1: 2, 4: 6}
}
n=5
import heapq
def Dijkstra(graf, start):
    global pred
    #dictionar cu nodurile si infinit prima oara
    distante = {nod: float('infinity') for nod in graf}

    #seteaza distanta de la nodul de start 0
    distante[start] = 0

    # pastreaza distantele de la nodul de start la cel curent
    heap = [(0, start)]
    while len(heap) > 0:
        #extrage pe rand din heap
        dist, nod = heapq.heappop(heap)
        if dist <= distante[nod]:
            #ia vecinii nodului curent
            for vecin, cost in graf[nod].items():
                if dist+cost < distante[vecin]:
                    parent[vecin]=nod
                    distante[vecin] = dist+cost
                    heapq.heappush(heap, (dist+cost, vecin))

    return distante
#distanta de la nodul de start la celelalte noduri
s=1
t=2
parent=[-1]*(n+1)
distanta=Dijkstra(graf, s)
def printPath():
    global parent, t
    if parent[t]==-1:
        return
    print(t, end=" ")
    t=parent[t]
    printPath()

print(distanta)
print("distanta minima este", distanta[t])
#vreau si drumul
print("drumul este:", s, end=" ")
printPath()
