'''
CICLU IN GRAF N FOLOSIND DF
    graf neorientat (poate fi si neconex)
    afisare ciclu
    folosesc DF
'''
#de la a la b si de la b la a
n=7
m=8
la={1: [3],
    2: [4],
    3: [1, 4, 5, 6, 7],
    4: [2, 3],
    5: [3, 6],
    6: [3, 5, 7],
    7: [6, 3]
    }
viz=[0]*(n+1)
parcurg=[]
tata=[0]*(n+1)
ok=0
def DF(x):
    global ok
    viz[x]=1
    if ok==0:
        for i in range (len(la[x])):
            y=la[x][i]
            if viz[y]==0:
                tata[y]=x
                parcurg.append(y)
                DF(y)
                if ok==1:
                    return
            elif y != tata[x]:
                print("ciclu elementar")
                v=x
                nr=1
                while v!=y:
                    print(v, end=" ")
                    nr+=1
                    v=tata[v]
                print(y, x, sep=" " )
                #print("lungime ciclu: ", nr)
                ok=1

start=1
DF(start)
print(parcurg)
if ok==0:
    print("graf aciclic")
