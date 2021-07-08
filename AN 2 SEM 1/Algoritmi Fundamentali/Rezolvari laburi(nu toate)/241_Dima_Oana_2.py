'''
    Graf orientat  fara circuite 1.
    costul poate fi si negativ 2.
    din 1. + 2. => algoritm DAG
    => algoritm pt drumuri minime de sursa unica in grafuri aciclice si arce de cost negativ
    Complexitate O(m+n)
'''
#citire din fisier
f=open("graf.in")
line=f.readline()
v=line.split()
n=int(v[0])
m=int(v[1])
def Liste(muchii, noduri):
    l={}
    for i in range(1,noduri+1):
        l[i]=[]

    for i in range(muchii):
       line=f.readline()
       v=line.split()
       l[int(v[0])].append((int(v[1]), int(v[2])))
    return l
graf=Liste(m,n)
line=f.readline()
v=line.split()
s1=int(v[0])
s2=int(v[1])
f.close()
def aux(nod, viz, sortate): #functie auxiliara pt sortare topologica
    global n, graf
    viz[nod] = 1 #marcheaza nodul ca vizitat
    #ia toate nodurile adiacente nevizitate ale lui nod
    if nod in range(1, n+1):
        for i, cost in graf[nod]:
            if viz[i] == 0:
                aux(i, viz, sortate)
    sortate.append(nod)

def topologicalSort():
    global n, graf
    #initializare
    viz = [0] * (n+1)
    sortate = []

    for i in range(1,n+1): #iau toate nodurile pe rand
        if viz[i] == 0:
            aux( i, viz, sortate)
    return sortate
def DAG(start):
    global n, graf
    dist = [float("Inf")] * (n + 1)
    dist[start] = 0
    tata = [0] * (n + 1)

    # sortez topologic
    sortata = topologicalSort()

    while sortata:
        i = sortata.pop()
        # iau nodurile adiacente cu i si le calculez distanta
        for nod, cost in graf[i]:
            if dist[i] + cost< dist[nod]:
                dist[nod] = dist[i] + cost
                tata[nod] = i
    return dist, tata

d1, t1=DAG(s1)
d2, t2=DAG(s2)
dist_min=float("Inf")
v=None
for i in range(1, n+1):
    #primul nod care are distanta din s1 egala cu distanta din s2
    #plus sa fie cel mai apropiat intre cele 2 surse
    if d1[i]==d2[i] and d1[i]<dist_min:
        dist_min=d1[i]
        v=i
        print("a)\nv=", i)
        break
if v==None:
    print("a)\nNu exista ")
else:
    print("b)")
    copy=v
    def DRUM(s1, tata, c): #afisare  drum
        print(c, end=" ")
        while s1!=tata[c]:
            print(tata[c], end=" ")
            c=tata[c]
        else:
            print(tata[c], end=" ")
    DRUM(s1, t1, copy)





