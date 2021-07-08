'''
    Drumuri minime de sursa unica
    graf ponderat cu cost pozitiv si poate contine circuite
    vrea Dijkstra cu puncte de control
    si un nod dat
    cel mai apropiat punct de control fata de acel nod
    O(m log n)
'''
graf = {
    1: {2: 15, 3: 11},
    2: {1: 15, 5: 10, 6: 5, 4: 3},
    3: {1: 11, 5: 8, 6: 9},
    4: {2: 3, 6: 2},
    5: {2: 10, 6: 20, 3: 8},
    6: {3: 9, 5: 20, 2: 5, 4: 2}
}
n=6
import heapq
def Dijkstra(graf, start):
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
                    distante[vecin] = dist+cost
                    heapq.heappush(heap, (dist+cost, vecin))

    return distante
#distanta de la nodul de start la celelalte noduri
start=2
puncte_control=[1, 3,6]
distante=Dijkstra(graf, start)
print(distante)
min=99999999999
punct_apropiat=None
for i in range(1,n+1):
    if i in puncte_control and distante[i]<min:
        min=distante[i]
        punct_apropiat=i
print("cel mai apropiat punct de control de start este: ", punct_apropiat)