'''
 Lee Alg pt matrice
 se da o matrice, p puncte marcate cu 1
 distanta Manhatattan (d(a,b) masurata pe oriz & vert)
 se dau q puncte
 sa se calculeze pt fiecare q puncte cea mai apropiata distanta marcata cu 1

'''
f=open("input.txt")
line=f.readline()
v=line.split()
n=int(v[0])
m=int(v[1])
final=[] #plec din punctele de start si trebuie sa ajung in final
def Matrice(n,m):
    matrice=[]
    for i in range (n):
        ma=[]
        line=f.readline()
        v=line.split()
        for j in range(m):
            ma.append(int(v[j]))
            if int(v[j])==1:
                final.append((i+1,j+1))
                ma.append(-1)
            else:
                ma.append(0)
        matrice.append(ma)

    return matrice
matrice=Matrice(n,m)

start=[]
for x in f.readlines():
    v=x.split()
    start.append((int(v[0]), int(v[1])))

f.close()
                #Lee algh
#vectori de pozitii  axa oy si ox N, S, V E
di=[0,0,1,-1]
dj=[1,-1,0,0]

def ok(i,j):
    #daca o coordonata este buna sau nu
    if i<0 or j<0 or i>=n or j>=m:
        return False
    if (i+1,j+1) in final: #daca intalneste un copac
        return False
    return True
def lee(startx, starty, matrice):
    from collections import deque
    coada = deque([])  # coada de perechi

    matrice[startx][starty]=1
    coada.append((startx, starty))
    while len(coada)>0:
        pair=coada.popleft()
        i=pair[0]
        j=pair[1]

        for directie in range(0,4):
            i_urm=i+di[directie]
            j_urm=j+dj[directie]

            if ok(i_urm, j_urm) == True and matrice[i_urm][j_urm]<1:

                matrice[i_urm][j_urm]=matrice[i][j]+1
                #x pasi necesari ca sa ajung in p
                #vecinul lui p face x+1 pasi
                coada.append((i_urm, j_urm))
            elif (i_urm+1, j_urm+1) in final:
                print(matrice[i][j], " ", "[", i_urm+1, ",", j_urm+1, "]")
                coada=deque([])
                break


for tuple in start:
    copy=matrice
    lee(tuple[0]-1, tuple[1]-1, copy)