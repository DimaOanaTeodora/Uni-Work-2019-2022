'''
    lee Alg pt matrice -> problema Romeo si Julieta
    vor sa det un punct optim de intalnire
    matrice n linii m col = harta oras
    marcate cu spatiu zonele prin care se poate trece
    cu x zonele prin care nu se poate trece
    R locul lui Romeo & J locul lui Julieta
    deplasare oriz/vert/diag
    vor un punct de intalnire ca sa ajunga in ac timp
'''
f=open("RJ.txt")
line=f.readline()
v=line.split()
n=int(v[0])
m=int(v[1])
def zero(n,m): #matrice de n*m cu zerouri
    matrice=[]
    for i in range(n):
        ma=[]
        for j in range(m):
            ma.append(0)
        matrice.append(ma)
    return matrice
romeo=zero(n,m)
julieta=zero(n,m)

#modifica matricile pentru amandoi
for i in range(n):
    line=f.readline()
    #-1 pe unde e x
    # 99999999 daca e locuinta lui romeo in matricea julietei si invers
    for j in range (m):
        if line[j]=='R':
            romeo[i][j]=0
            rlin=i
            rcol=j
            julieta[i][j]=99999999
        elif line[j]=='J':
            romeo[i][j] = 99999999
            jlin = i
            jcol = j
            julieta[i][j] = 0
        elif line[j]=='X':
            romeo[i][j]=julieta[i][j]=-1
        else:
            romeo[i][j] = julieta[i][j] = 99999999
f.close()

                #Lee algh
#vectori de pozitii  axa oy si ox N, S, V E, N-V, S-v...
di=[0,0,1,-1,1,1,-1,-1]
dj=[1,-1,0,0,1,-1,1,-1]

def ok(i,j):
    #daca o coordonata este buna sau nu
    if i<0 or j<0 or i>=n or j>=m:
        return False
    return True
from collections import deque
coada = deque([])  # coada de perechi
def lee(M):

    while len(coada)>0:
        pair=coada.popleft()
        i=pair[0]
        j=pair[1]

        for directie in range(0,8):
            i_urm=i+di[directie]
            j_urm=j+dj[directie]

            if ok(i_urm, j_urm) == True and M[i_urm][j_urm]> M[i][j]+1:
                M[i_urm][j_urm]=M[i][j]+1
                #x pasi necesari ca sa ajung in p
                #vecinul lui p face x+1 pasi
                coada.append((i_urm, j_urm))

coada.append((rlin,rcol))
lee(romeo)
coada.append((jlin,jcol))
lee(julieta)

rezl=1
rezc=1
mini=999999999
for i in range(n):
    for j in range(m):
        if romeo[i][j]==julieta[i][j] and romeo[i][j]!=-1 and romeo[i][j]<mini:
            rezl=i+1
            rezc=j+1
            mini=romeo[i][j]
print(romeo[rezl-1][rezc-1]+1, rezl, rezc, sep=" ")




