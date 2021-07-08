'''
    n numarul de activitati
    d1, d2,d3 durata activitati
    m perechi activitatea i trebuie sa se incheie inainte de j
    timpul minim de finalizare al proiectului este costul maxim al unui
    drum de la S la T
    DRUM CRITIC=drum de cost maxim de la S la T
    timpul minim de inceput al unei activitati u
    costul maxim al unui drum de la S la u
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
    1:[(2,7)],
    2:[(6,4), (3,4)],
    3:[(5,30),(6,30)],
    4:[(3,12)],
    5:[],
    6:[]

}
#incep de la 1 la n
durata=[7,4,30,12,2,5]
#initializari
start=0
dist = [-float("Inf")] * (n+2)
dist[start] = 0
tata=[0]*(n+2)

#sortez topologic
sortata=topologicalSort()
#legaturile cu S si T
graf[0]=[(1,0), (4,0)] #legaturi s
graf[5]=[(7, 2)]  # legaturi t
graf[6]= [(7, 5)] # legaturi t
graf[7]=[]

sortata=[0]+sortata+[7]

#!!Important sortarea topologica se comporta ca o coada
from collections import deque
sortata=deque(sortata)

durata_min=0 #calculez maximul
nodul_cu_durata_min=None
while sortata:
    i = sortata.popleft()
    #iau nodurile adiacente cu i si le calculez distanta
    if i in range(0, n+2):
        for node, weight in graf[i]:
            if dist[i] + weight> dist[node] : #inversez conditia fata de bellman ford normal
                dist[node] = dist[i] + weight
                '''
               timpul minim de finalizare al proiectului este costul maxim al unui
    drum de la S la T
                '''
                if durata_min < dist[node]:
                    durata_min=dist[node]
                    nodul_cu_durata_min=node
                tata[node]=i
print("Durata minima a proiectului este: ", durata_min)
print("Vectorul de distante este: ",dist)
print("Vectorul de tati este: ", tata)

#afisez drumul critic =activitatiel critice
#plec pe vectorul de tati de la nodul_cu_durata_min
print("Activitatiel critice: ", end=" ")
while tata[nodul_cu_durata_min]!=0:
    print(tata[nodul_cu_durata_min], end=" ")
    nodul_cu_durata_min=tata[nodul_cu_durata_min]
print("\nIntervalele de desfășurare pentru fiecare activitate: ")
#de printat intervalele de desfasurare
#activitatea x incepe la momentul d[x] (distanta fata de start calculata)
#si se termina la d[x]+durata(x)
for i in range(1, n+1):
    print(i, ": (", dist[i], ",", dist[i]+durata[i-1] , ")")

