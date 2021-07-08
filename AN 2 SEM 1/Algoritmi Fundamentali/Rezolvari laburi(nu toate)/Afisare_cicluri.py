'''
    se da un graf orientat
    sa se afiseze ciclurile sale
'''

def dfs_cycle():
    global graph, cyclenumber, cycles, u, p, color, mark, par, N

    if color[u] == 2:
        return
    if color[u] == 1:
        cyclenumber += 1
        cur = p
        mark[cur] = cyclenumber

        while cur != u:
            cur = par[cur]
            mark[cur] = cyclenumber
        return
    par[u] = p

    color[u] = 1
    for v in range(N):
        if graph[u][v]!=0 and v == par[u]:
            continue
        dfs_cycle()

    color[u] = 2


def printCycles():
    global graph, cyclenumber, cycles, u, p, color, mark, par, edges, N
    for i in range(len(mark)):
        if mark[i] != 0:
            cycles[mark[i]].append(i)

    for i in range(len(cycles)):
        print("Cycle Number %d:" % i, end=" ")
        for x in cycles[i]:
            print(x, end=" ")
        print()

N=6
graph= [
#    s  1  2  3  4  t
    [0, 0, 0, 0, 0, 0], #s
    [0, 0, 1, 0, 1, 0], #1
    [0, 1, 0, 1, 0, 0], #2
    [0, 0, 1, 0, 1, 0], #3
    [0, 1, 0, 1, 0, 0], #4
    [0, 0, 0, 0, 0, 0]  #t
        ]
color = [0] * N
par = [0] * N
mark = [0] * N
cyclenumber = 0
cycles=[[] for i in range(N)]
u=1
p=0
dfs_cycle()
printCycles()