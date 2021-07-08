'''
    Fluxuri maxime in retele de transport
    implementare folosind Bf
    varianta cu graf rezidual
'''
from collections import deque
def bfs():
    global graf, graf_r, start, final
    #extragere drum
    coada = deque([start])
    drumurile = {start: []}
    if start == final:
        return drumurile[start]
    while len(coada):
        u = coada.popleft()
        for v in range(len(graf)):
            if (graf[u][v] - graf_r[u][v] > 0) and (v not in drumurile):
                drumurile[v] = drumurile[u] + [(u, v)]
                if v == final:
                    return drumurile[v]
                coada.append(v)
    return None
def max_flow():
    global graf, start, graf_r,n
    drum = bfs()
    while drum != None:
        flow = min(graf[u][v] - graf_r[u][v] for u, v in drum)
        for u, v in drum:
            graf_r[u][v] += flow #arc direct
            graf_r[v][u] -= flow #arc invers
        drum = bfs()
    S=0 #suma fluxuri
    for i in range(n):
        S+=graf_r[start][i]
    return S

n=6
# graf dat prin matricea de capacitati
#     s  1  2  3  4  t
graf = [[0, 6, 0, 8, 0, 0],  # s
     [0, 0, 4, 0, 3, 0],  # 1
     [0, 0, 0, 0, 0, 7],  # 2
     [0, 0, 0, 0, 4, 2],  # 3
     [0, 0, 0, 0, 0, 9],  # 4
     [0, 0, 0, 0, 0, 0]]  # t

start = 0  # S
final = 5  # T
#declarare graf rezidual
graf_r = [[0] * n for i in range(n)]
print("Max flow: ", max_flow())
print("matrice graf rezidual:", graf_r)

'''
fluxul pt fiecare arc se ia din graful rezidual final:
pentru arcul xy de pe arcul yx din graful rezidual
'''