'''
 1.matrice de adiacenta pt un graf o/no
 2.liste de adiacenta pt un graf o/n
 3. trecere de la una la alta
 -> nu am param care sa specifice daca e o/no
 -> nu am subprogram de afisare a matricei/listei
 citit din fisierul graf.in
'''
f=open("graf.in")
line=f.readline()
v=line.split()
#pe prima linie nr noduri si nr muchii
n=int(v[0])
m=int(v[1])
        # 1 matrice de adiacenta
def Matrice(muchii, noduri):
    matrice=[]
    for i in range (noduri):
        m=[]
        for j in range(noduri):
            m.append(0)
        matrice.append(m)
    for i in range(muchii):
        line=f.readline()
        v=line.split()
        matrice[int(v[0])-1][int(v[1])-1]=1
        matrice[int(v[1])-1][int(v[0])-1] = 1
    return matrice
matrice=Matrice(m,n)
f.close()

f=open("graf.in")
line=f.readline()
v=line.split()
#pe prima linie nr noduri si nr muchii
n=int(v[0])
m=int(v[1])
        # 2 lista de adiacenta
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
        # 3 trecere de la una la alta
def trec_ML(matrice, noduri):
    lista={}
    for i in range(1,noduri+1):
        lista[i]=[]
    for i in range(noduri):
        for j in range(noduri):
            if matrice[i][j]==1:
                lista[i+1].append(j+1)
                lista[j+1].append(i+1)
    return lista
print(trec_ML(matrice,n))

def trec_LM(lista, noduri):
    matrice=[]
    for i in range(noduri):
        m=[]
        for j in range(noduri):
            m.append(0)
        matrice.append(m)
    for i in range(1,noduri+1):
        v=lista[i]
        for x in v:
            matrice[i-1][x-1]=1
            matrice[x-1][i-1]=1
    return matrice
print(trec_LM(lista,n))