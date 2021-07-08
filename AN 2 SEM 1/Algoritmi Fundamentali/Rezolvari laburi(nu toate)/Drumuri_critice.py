'''
    Drum critic = drum de cost maxim de la S la T
    Planificare activitati
    timp minim de inceput al u= cost maxim al unui drum de la s la u
    ma folosesc de DAG
'''
def aux(nod, viz, sortate):
    global n, graf
    viz[nod] = True #marcheaza nodul ca vizitat
    #ia toate nodurile adiacente nevizitate ale lui nod
    if nod in graf.keys():
        for (i, cost) in graf[nod]:
            if viz[i] == False:
                aux(i, viz, sortate)
    sortate.insert(0, nod)

def topologicalSort():
    global n, graf
    #initializare
    viz = [False] * (n+1)
    sortate = []

    for i in range(1,n+1): #iau toate nodurile pe rand
        if viz[i] == False: # le vizitez
            aux(i, viz, sortate)
    return sortate

n=6
graf={
    1:[(2,7)],
    2:[(6,4), (3,4)],
    3:[(5,30),(6,30)],
    4:[(3,12)],
    5:[(2,7)],
    6:[(5,7)]
}

#sortez topologic
sortata=topologicalSort()

#adaug pe s si pe t
graf[0]=[(1,0), (4,0)] #S
graf[7]=[] #t

#initializari
start=0
dist = [-float("Inf")] * (n+2)
dist[start] = 0
tata=[0]*(n+2)
sortata=[0]+sortata+[7]
print(sortata)
sortata= [0, 1, 4, 2, 3, 5, 6, 7]
#aici se modifica fata de DAG
for u in sortata:
    for (v,w) in graf[u]:
        if dist[u]+w > dist[v]:
            dist[v]=dist[u]+w
            tata[v]=u

print("Vectorul de distante este: ",dist)
print("Vectorul de tati este: ", tata)