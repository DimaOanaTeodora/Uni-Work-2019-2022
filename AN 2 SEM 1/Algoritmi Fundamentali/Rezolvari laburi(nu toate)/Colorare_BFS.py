'''
    Colorare graf cu max k culori in O(m+n)
    folosind BFS
'''
from collections import deque
def coloreaza():
    global graf, viz, culori
    nr_max_culori=1
    for nod in range (n):
        if viz[nod]==1:
            continue
        viz[nod]=1
        coada=deque([nod])
        #BFS
        while len(coada)>0:
            u=coada.popleft()
            #verific toate nodurile adiacente cu top
            for v in range(n):
                if graf[u][v]!=0:
                    if culori[u]==culori[v]:
                        culori[v]+=1
                    nr_max_culori=max(nr_max_culori, max(culori[u], culori[v]))
                    if nr_max_culori>k:
                        return False
                    if viz[v]==0:
                        viz[v]=1
                        coada.append(v)
    return True
n=4
#IMI E MAI USOR SA LUCREZ DE LA 0
graf=[
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]
k=3 #numarul maxim de culori

culori=[1]*n
viz=[0]*n
if coloreaza()==True:
    print("colorarea este posibila")
    print("vectorul de culori:", culori, sep=" ")
else:
    print("colorarea nu e posibila")


