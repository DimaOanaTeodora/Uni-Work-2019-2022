'''
DRUMURI MINIME FOLOSIND BF
    determinarea mai multor lanturi minime intre doua varfuri u si v
    folosesc dictionar de tati
    graf neorientat
    folosesc BF
'''
#de la a la b si de la b la a
lista={1: [2, 4],
       2: [1, 3, 5],
       3: [2, 6, 8, 5],
       4: [1, 6],
       5: [2, 3, 8],
       6: [3, 4, 7],
       7: [6, 8],
       8: [3, 7, 5]}
n=8
m=11
#u si v date de la tastatura
print("dati cele doua noduri: ")
u=int(input())
v=int(input())

viz=[0]*(n+1)
tata={}
for i in range (1,n+1):
    tata[i]=[]
d=[None]*(n+1)
parcurg=[]
def BF(s):
    from collections import deque
    q=deque([])
    q.append(s)
    viz[s]=1
    d[s]=0
    while len(q)>0:
        x=q.popleft()
        parcurg.append(x)
        for j in lista[x]:
            if viz[j]==0:
                q.append(j)
                viz[j]=1
                tata[j].append(x)
                d[j]=d[x]+1
            elif d[j]==d[x]+1:
                tata[j].append(x)


BF(u)
c=[]
def LANT(s):
        c.append(s)
        if s==u:
            while len(c)>0 and len(tata[c[-1]])<=1:
                print(c.pop(), end=" ")
            if len(c)>0:
                c.reverse()
                print(*c)
                c.reverse()
            print()

        for t in tata[s]:
            LANT(t)

LANT(v)
