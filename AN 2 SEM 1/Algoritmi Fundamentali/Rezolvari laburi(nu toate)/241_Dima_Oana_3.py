'''
    n monitoare
    m depozite
    pt fiecare fabrica => cate monit au fost produse
    pt fiecare depozit => cate monitoare poate depozita
    contracte intre fabrica si depozit
    Graf bipartit
    det cuplaj maxim
    Testare graf bipartit folosind BFS
    Cuplajul maxim folosindu-ma de bipartitie si de EK
    pentru fiecare arc cu flux nenul xy din N care nu este
    incident în s sau t, muchia xy corespunzătoare din G se
    adaugă la M)
    fac varianta cu graf rezidual
'''
#citire din fisier
f=open("fabrici.in")
line=f.readline()
v=line.split()
n=int(v[0])
m=int(v[1])
cant_mon=[]
line=f.readline()
v=line.split()
for i in range(n):
    cant_mon.append(int(v[i]))
nr_mon=[]
line=f.readline()
v=line.split()
for i in range(m):
    nr_mon.append(int(v[i]))
line=f.readline()
v=line.split()
k=int(v[0])
def matrice(muchii, noduri):
    l=[]
    for i in range(noduri+1):
        m=[]
        for j in range(noduri+1):
            m.append(0)
        l.append(m)

    for i in range(muchii):
       line=f.readline()
       v=line.split()
       a=int(v[0])
       b=int(v[1])
       c=int(v[2])
       #l[a][b]=c
    return l
graf=matrice(k,n)
f.close()
        #sfarsit citire
def BFS():
    global graf, s, t, n, parent
    visited = [False] * (n+2)
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graf[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return True if visited[t] else False

def FordFulkerson():
    global graf, s, t, n, parent

    max_flow = 0

    while BFS():
        path_flow = float("Inf")
        cs = t
        while cs != s:
            path_flow = min(path_flow, graf[parent[cs]][cs])
            cs = parent[cs]

        max_flow += path_flow

        v = t
        while v != s:
            u = parent[v]
            graf[u][v] -= path_flow #arc direct
            graf[v][u] += path_flow #arc invers
            v = parent[v]

    return max_flow
def BIPARTIT():
    global n, graf, start, culoare
    culoare[start] = 1 #colorez primul nod (o sa alternez culorile 0 si 1 )

    coada = []
    coada.append(start)

    while len(coada)>0:
        u = coada.pop()
        if graf[u][u] == 1: #daca s-a scos pe sine
            return False
        for v in range(1,n+1):
            if graf[u][v] == 1 and culoare[v] == -1:#nu a fost colorat
                culoare[v] = 1 - culoare[u]
                coada.append(v)
            #muchie de la u la v cu u si v cu aceeasi culoare => nu e bipartit
            elif graf[u][v] == 1 and culoare[v] == culoare[u]:
                return False
    return True