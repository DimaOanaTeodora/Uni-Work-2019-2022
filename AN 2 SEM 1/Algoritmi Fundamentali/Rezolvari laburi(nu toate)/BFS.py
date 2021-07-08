'''
    parcurgere in latime graf o/n
    pt graf neorientat
'''
#de la a la b si de la b la a
n=4
m=4
la={0:[1,2],
    1: [0,3],
    2: [0,3],
    3: [1, 2]

    }
viz=[0]*(n+1)
tata=[0]*(n+1)
d=[None]*(n+1)#lungime drumuri d[j]=nivel j in arborele parcurgerii d[j]=d[tata[j]]+1
parcurg=[]

def BF(s):
    global la, tata, viz, d, parcurg
    q=[]
    q.append(s)
    viz[s]=1
    d[s]=0
    while len(q)>0:
        x=q.pop(0)
        parcurg.append(x)
        for j in la[x]:
            if viz[j]==0:
                q.append(j)
                viz[j]=1
                tata[j]=x
                d[j]=d[x]+1


    #parcurgere BF
start=0
BF(start) #pt start=1 testez daca toate nodurile au fost vizitate=> graf conex
print("vectorul de tati: ",*tata) #arborele pe vectorul de tati
print("parcurgere bfs: ", *parcurg)
print(d)