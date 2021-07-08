'''
DRUM MIN FOLOSIND BF
    se da un graf cu n noduri + care sunt punctele de control
    se da un nod de la tastatura
    vrea cel mai apropiat punct de control de acesta
    + un lant minim pana la acesta
    O(n+m)
    a) pt graf neorientat
    b) graf orientat (acelasi algoritm)
    Utilizez: BF
    9 11
1 2
1 3
1 4
2 5
2 9
3 5
3 7
5 7
6 7
6 8
4 6
'''
            #citire
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
lista=Liste(m,n)
f.close()

#citire puncte de control de la tastatura
line=input("dati punctele de control: ")
v=line.split()
puncte=[]
for x in v:
    puncte.append(int(x))

#citire punct de start tot de la tastatura
line=input("dati nodul de start: ")
start=int(line)

#de facut vector de vizitat si pentru puncte
    #pe masura ce citim verificam daca e punct de control si-l vizitam
viz=[0]*(n+1)
tata=[0]*(n+1)
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
                tata[j]=x
                d[j]=d[x]+1
        if parcurg[-1] in puncte:
            break


BF(start)
print(lista)
print("parcurgere BF este: ", *parcurg)

print("cel mai apropiat punct de control este: ", parcurg[-1], "\n lantul este: ", end=" ")
        #lantul din orice arbore folosind vectorul de tati
def LANT(s):
    while s!=0:
        print(s, end=" ")
        s=tata[s]

LANT(parcurg[-1])


