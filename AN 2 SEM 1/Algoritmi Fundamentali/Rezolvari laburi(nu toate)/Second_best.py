'''
    Al doilea APCM
    gasesc muchia_maxima=costul maxim al unei muchii in lantul de la u la v
    gasesc muchia_noua care nu e parte din APCM,
    dar care are min( abs(max- cost(muchia_noua)))
    returnez noul APCM T'=T-muchia_maxima + muchia_noua
'''
def reuneste(u,v):
    global r,n
    r1=r[u] #culoarea nodului u
    r2=r[v] #culoarea nodului v
    for k in range (1,n+1):
        if r[k]==r2: #coloram restul componentelor
            r[k]=r1
#de la a la b si invers

#muchii=[(1, 4, 1),(1, 3, 5),(1, 2, 10), (2, 3, 2),(4, 2, 6), (4, 5, 12), (5, 2, 11)]
muchii=[(1,2,13), (1,3,14), (2,3,16), (1,4,11), (1,5,12), (4,5,15), (5,6,10)]
graf={1:[(2,13), (3,14), (4,11), (5,12)],
      2:[(1,13), (3,16)],
      3:[(1,14), (2,16)],
      4:[(1,11),(5,15)],
      5:[(1,12), (4,15), (6,10)],
      6:[(5,10)]}
n=6 #noduri
#sortez crescator dupa cost
muchii=sorted(muchii, key=( lambda t: t[2]))

#initializez
r=[0] #'colorez' componentele
for i in range(1,n+1):
    r.append(i)
nrmsel=0
cost=0
arbore=[]

#trebuie sa formez graful APCM rezultat
T={}
for i in range(1, n+1):
    T[i]=[]
for m in muchii:
    if r[m[0]] != r[m[1]]: #daca nu fac parte din ac componenta (adica nu avem ciclu)
        T[m[0]].append((m[1], m[2]))
        T[m[1]].append((m[0], m[2]))
        arbore.append((m[0], m[1]))
        reuneste(m[0], m[1])
        cost=cost+m[2]
        nrmsel=nrmsel+1
        if nrmsel==n-1: #ca sa fie arbore trebuie sa aiba n-1 muchii
            break
print("Primul APCM este:\n ", *arbore)
print("Costul este: ", cost)

def BF(s):
    global T, viz, tata, parcurg
    q=[]
    q.append(s)
    viz[s]=1
    while len(q)>0:
        x=q.pop(0)
        parcurg.append(x)
        for (j,w) in T[x]:
            if viz[j]==0:
                q.append(j)
                viz[j]=1
                tata[j] = x
def lant(s,f):
    global T, tata
    max=(0,0,0)
    while s!=f:
        a=s
        b=tata[s]
        for (nod, w) in T[s]:
            if nod==b:
                if w>max[2]:
                    max=(a,b,w)
                break
        s=tata[s]
    return max
dif_min=99999999999
muchie_de_scos=None
muchie_inlocuire=None
for i in range (1, n+1):
    tata=[0]*(n+1)
    viz=[0]*(n+1)
    parcurg=[]
    BF(i)
    max = [(0, 0, 0)] * (n + 1)
    for x in parcurg[1:]:
        M = (0, 0, 0)
        a=x
        while a != i:
            b = tata[a]
            for (nod, w) in T[a]:
                if nod == b:
                    if w > M[2]:
                        M = (a, b, w)
                    break
            a = tata[a]
        #de la i la x
        #print("i si x", i, x, sep=" ")
        max[x]=M
        #trebuie sa le iau muchiile care nu sunt in arbore
        exista=0
        for (nod, w) in T[i]:
            if nod==x:
                exista=1
                break
        if exista==0:
            for (nod, w) in graf[i]:
                if nod==x:
                    dif=w-M[2]
                    #print("dif_min", dif_min)
                    if dif < dif_min:
                        dif_min=dif
                        muchie_inlocuire=(i,nod, w)
                        muchie_de_scos=M
                        #print("dif: ", dif)
                        #print("muchie inloc= ", muchie_inlocuire)
                        #print("M: ", M)
                    break
    #print("i=", i, max[1:])
#fac noul arbore (doar din afisare)
print("Al doilea APCM")
for x in arbore:
    if x[0] in muchie_de_scos and x[1] in muchie_de_scos:
        print(muchie_inlocuire[0], muchie_inlocuire[1], sep=" ")
    else:
        print(x[0], x[1], sep=" ")
cost=cost-muchie_de_scos[2]
cost=cost+muchie_inlocuire[2]
print("Costul este: ", cost)
