'''
    graf neroeintat conex
    T1 arbore de distante => parcurgere BFS
    T2 nu e arbore de distante => arbore oarecare =>parcurgere DFS
    Complexitate O(m)
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
       l[int(v[0])].append(int(v[1]))
       l[int(v[1])].append(int(v[0]))
    return l
la=Liste(m,n)
line=f.readline()
s=int(line)
f.close()

def BF(s): #alg parcurgere in latime => arbore de distante
    global la, tata, viz, d, parcurg
    q=[]
    q.append(s)
    viz[s]=1
    d[s]=0 #vizitez nodul de start
    while len(q)>0:
        x=q.pop(0)
        for j in la[x]:
            if viz[j]==0:
                parcurg.append((x,j)) #adaug muchia pt care j e adiacent cu nodul curent x
                q.append(j)
                viz[j]=1
                tata[j]=x #il adaug pe x ca tata al lui j
                d[j]=d[x]+1 #cresc distanta cu o unitate


viz=[0]*(n+1)
tata=[0]*(n+1)
d=[0]*(n+1)
parcurg=[]
BF(s)

print("T1: ")
for muchie in parcurg:
    print(muchie[0], muchie[1], sep=" ")

#pt T2
arbore_oarecare=[]
def DF(x): #alg parcurgere in adancime => arbore oarecare
    global la, vizz, tataa
    vizz[x] = 1
    for y in la[x]:
        if vizz[y] == 0:
            arbore_oarecare.append((x,y))
            tataa[y] = x
            dist[y] = dist[x] + 1 #calculez distanta
            DF(y)

vizz=[0]*(n+1)
tataa=[0]*(n+1)
dist=[0]*(n+1)
DF(s)
print("T2:")
for muchie in arbore_oarecare:
    print(muchie[0], muchie[1], sep=" ")

#caut un varf u pt care distanta de la s la u din G e diferita pt distanta de la s la u din T2
print("u =", end=" " )
for i in range(1, n+1):
    if d[i]!=dist[i]:
        print(i)
        break