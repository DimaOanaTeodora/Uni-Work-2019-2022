'''
    parcurgere in adancime (ca din floare in floare) graf o/n
    aici graf orientat
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


def DF(x):
    global la, viz, tata
    viz[x] = 1
    for y in la[x]:
        if viz[y] == 0:
            print(y, end=" ")
            tata[y] = x
            DF(y)
start=1
DF(start)
#afisare arbore df
def LANT(s):
    while s!=0:
        print(s, end=" ")
        s=tata[s]
LANT(start)
