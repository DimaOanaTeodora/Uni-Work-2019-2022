'''
    APCM folosind Prim
    graf neorientat
    O(m log n)
    folosesc dictionar de seturi nod1: { nod2: cost}
'''
from collections import defaultdict
import heapq
graf = {
    1: {2: 28, 6: 10},
    2: {1: 28, 3: 16, 7: 14},
    3: {2: 16, 4: 12},
    4: {3: 12, 5: 22, 7: 18},
    5: {4: 22, 7: 24, 6: 25},
    6: {1: 10, 5: 25},
    7: {2: 14, 4: 18, 5:24}
}
start=1
arbore = defaultdict(set)

#vector noduri vizitate
viz = set([start])

#ia muchiile care incep din A
muchii = [(cost, start, b) for b, cost in graf[start].items()]

#ordonare folosind heap
heapq.heapify(muchii)

cost_total=0
while muchii:
        #extrage cate un tuplu
        cost, a, b = heapq.heappop(muchii)
        #daca al doilea nod nu a fost vizitat
        if b not in viz:
            cost_total=cost_total+cost
            viz.add(b) #il viziteaza
            arbore[a].add(b) #il adauga in arbore (practic muchia (a,b))
            for x, cost in graf[b].items():#ia toate nodurile care pornesc din to
                if x not in viz: #daca nu au fost vizitate
                    heapq.heappush(muchii, (cost, b, x)) #le adauga in heap

arbore=dict(arbore)
print("Arborele este: ")
for key in arbore.keys():
    for item in arbore[key]:
        print(key, item)
print("Costul este: ", cost_total)


