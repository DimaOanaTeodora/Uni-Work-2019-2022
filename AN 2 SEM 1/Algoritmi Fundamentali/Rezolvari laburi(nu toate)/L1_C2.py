'''
CIRCUIT IN GRAF O FOLOSIND DF
     n activitati numertotate de la 1 la n
     m perechi de activitati (a,b) activitatea a inaintea lui b
     testare proiect realizabil= nu exista dependente circulare intre activitatile sale
     daca proiectul nu se poate realiza sa se afiseze circuitele
     altfel mesajul 'REALIZABIL'
     graf orientat

'''
n=6
m=7
#doar de la a la b
la={1: [2, 5],
    2: [],
    3: [5],
    4: [6],
    5: [2, 4],
    6: [3]
    }
viz=[0]*(n+1)
tata=[0]*(n+1)
fin=[0]*(n+1)
ok=0
def DF(x):
    global la, ok, viz, tata, fin
    viz[x]=1
    for y in la[x]:
        if ok!=0:
            break
        if viz[y]==0:
            #print(y, end=" ") #asta e pt parcurgere
            tata[y]=x
            DF(y) ##pana aici parcurgere obisnuita
        elif fin[y]!=1:
                #y nu a fost finalizat este inca in explorare
                print("circuit elementar")
                #afisare lant de la x la y
                v = x
                while v != y:
                    print(v, end=" ")
                    v = tata[v]
                print(y, sep=" ")
                ok=1
    fin[x]=1 #finalizare explorare x

start=1
DF(start)
if ok==0:
    print("REALIZABIL")




