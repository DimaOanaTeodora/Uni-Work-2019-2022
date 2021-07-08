'''
    Testare graf bipartit folosind BFS
'''

def BIPARTIT():
    global n, graf, start, culoare
    culoare[start] = 1 #colorez primul nod (o sa alternez culorile 0 si 1 )

    coada = []
    coada.append(start)

    while len(coada)>0:
        u = coada.pop()
        if graf[u][u] == 1: #daca s-a scos pe sine
            return False
        for v in range(n):
            if graf[u][v] == 1 and culoare[v] == -1:#nu a fost colorat
                culoare[v] = 1 - culoare[u]
                coada.append(v)
            #muchie de la u la v cu u si v cu aceeasi culoare => nu e bipartit
            elif graf[u][v] == 1 and culoare[v] == culoare[u]:
                return False
    return True
n=4
graf= [[0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
        ]
start=0
culoare = [-1] * n
if BIPARTIT()==True:
    print("Graful este bipartit")
else:
    print("Graful NU este bipartit")
print(culoare)
M1=[]
M0=[]
#despart varfurile in 2 multimi in functie de culori
for i in range(n):
    if culoare[i]==1:
        M1.append(i)
    else:
        M0.append(i)
#S o sa fie legate de M1
#T o sa fie legat de M0