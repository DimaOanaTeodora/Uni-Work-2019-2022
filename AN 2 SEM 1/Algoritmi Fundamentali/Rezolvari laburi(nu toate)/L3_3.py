'''
    Clustering intre cuvinte
    ex: distanta de la (ana, care)=3
        ana-> cana -> cara -> care
    (de cate ori adauga sau inlocuieste fiecare litera)
    ex aici: adauga c, inlocuieste n-> r, inlocuieste a cu e => 3 operatii
    graf ponderat complet
    !!Lucrez de la 0
'''
def Levenshtein(a, b):
    #calculeaza distanta dintre 2 cuvinte date a si b
    if len(b)==0:
        return len(a)
    elif len(a)==0:
        return len(b)
    elif a[0]==b[0]:
        return Levenshtein(a[1:], b[1:])
    else:
        return 1+ min(Levenshtein(a[1:], b),
                      Levenshtein(a, b[1:]),
                      Levenshtein(a[1:], b[1:]))

cuvinte=["martian", "care", "este", "sinonim", "ana",
"case", "apa", "arbore", "partial", "minim"]
k=3 #nr de clase unice cerute
#trebuie sa fac lista de muchii
n=10
muchii=[]
#calculez distanta intre fiecare cuvant => graf ponderat complet
for i in range(n-1):
    for j in range(i+1, n):
        d=Levenshtein(cuvinte[i], cuvinte[j])
        muchii.append((i,j,d))

            #kruskal varianta 2
def reprez(u):
    #determinare radacina arbore care contine u
    global tata
    '''
    while tata[u] !=0:
        u=tata[u]
    return u
    '''
     #optimizare
    if tata[u] ==0:
        return u
    tata[u]=reprez(tata[u])
    return tata[u]


def reuneste(u,v):
    #reuniune ponderata
    global tata,h
    ru=reprez(u)
    rv=reprez(v)

    if h[ru]>h[rv]:
        tata[rv]=ru
    else:
        tata[ru]=rv
        if h[ru]==h[rv]:
            h[rv]=h[rv]+1


#initializare
tata=[0]*(n)
h=[0]*(n)

#sortez crescator dupa cost
muchii=sorted(muchii, key=( lambda t: t[2]))

nrmsel=0 #nr muchii selectate (arbore -> n-1 muchii)
cost=0
arbore=[]
i=0
while i< len(muchii):
   m=muchii[i]
   if reprez(m[0]) != reprez(m[1]): #daca nu fac parte din ac componenta (adica nu avem ciclu)
        #printez muchiile
        arbore.append((m[0], m[1]))
        reuneste(m[0], m[1])
        cost=cost+m[2]
        nrmsel=nrmsel+1

        if nrmsel == n - k:  # il opresc cand am pus n-k muchii
                            # ca sa am k clustere
            break
   i+=1

#afisare cuvinte
for i in range(n):
    if tata[i]==0:
        print(cuvinte[i], end=" ")
        for j in range(n):
            if tata[j]==i:
                print(cuvinte[j], end=" ")
        print()
#urmatoarea muchie pe care as fi selectat-o este gradul de separare
print("gradul se separare: ", muchii[i+1][2])


