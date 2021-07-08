'''
    Drumuri minime de sursa unica in grafuri aciclice
    merge si pe cost negativ
    O(m+n)
'''
def aux(nod, viz, sortate):
    global n, graf
    viz[nod] = True #marcheaza nodul ca vizitat
    #ia toate nodurile adiacente nevizitate ale lui nod
    if nod in graf.keys():
        for i, cost in graf[nod]:
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
            aux( i, viz, sortate)
    return sortate

n=6
graf={
    1:[(5,1),(6,2)],
    2:[],
    3:[(2,8),(5,4)],
    4:[(2,1)],
    5:[(2,7)],
    6:[(2,1)]
}

#initializari
start=3
dist = [float("Inf")] * (n+1)
dist[start] = 0
tata=[0]*(n+1)

#sortez topologic
sortata=topologicalSort()

while sortata:
    i = sortata.pop()
    #iau nodurile adiacente cu i si le calculez distanta
    if i in graf.keys():
        for node, weight in graf[i]:
            if dist[node] > dist[i] + weight:
                dist[node] = dist[i] + weight
                tata[node]=i


print("Vectorul de distante este: ",dist[1:])
print("Vectorul de tati este: ", tata[1:])