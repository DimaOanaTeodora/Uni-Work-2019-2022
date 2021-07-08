'''
   verific daca exista puncte critice (aici vulnerabile)
   daca nu exista => 'retea biconexa'
   radacina arborelui nu e punct critic => o excludem
   O(n+m)
'''

n=10
#doar de la a la b si de la b la a
la={1: [10, 5],
    2: [4,8,6],
    3: [5,6,7],
    4: [2,8],
    5: [1,3,6,9,10],
    6: [2,3,5,7],
    7: [3,6],
    8: [2,4],
    9: [5],
    10: [1,5]
    }

viz=[0]*(n+1)
niv_min=[0]*(n+1) #cat de sus putem ajunge din i mergand prin df
nivel=[0]*(n+1) #nivel[i] nivelul lui in arborele DF
puncte_critice=[]
start=1

def DF(x):
    global la, viz, niv_min, nivel, puncte_critice, start
    viz[x] = 1
    niv_min[x] = nivel[x]
    for y in la[x]:
        if viz[y] == 0:
            #(x,y) muchie de avansare
            nivel[y] = nivel[x] + 1
            DF(y)
            #actualizare niv_min[x]
            niv_min[x] = min(niv_min[x], niv_min[y])
            #testez daca (x,y) e muchie critica
            if niv_min[y] >= nivel[x] and x not in puncte_critice and x !=start:
                #radacina nu e punct critic deci o excludem
                puncte_critice.append(x)
        elif nivel[y]<nivel[x]-1: #(x,y) muchie de intoacere
            #actualizare niv_min[x]
            niv_min[x] = min(niv_min[x], nivel[y])


DF(start)
if len(puncte_critice)>0:
    print("punctele critice: ", *puncte_critice)
else:
    print("retea biconexa")
