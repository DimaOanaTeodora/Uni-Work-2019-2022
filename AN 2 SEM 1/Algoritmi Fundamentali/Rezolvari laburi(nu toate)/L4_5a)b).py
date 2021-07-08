'''
    detectare circuit negativ utilizand Floy-Warshall
'''
def floydWarshall():
    global w,d, n,p, INF, circuit, nod_circ
    for i in range(n):
        for j in  range(n):
            d[i][j]=w[i][j]
            if w[i][j]==INF:
                p[i][j]=0
            else:
                p[i][j]=i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j]>d[i][k]+d[k][j]:
                    #modific conditia pt inchiderea tranzitiva
                    #Roy Warshall
                    #d[i][j] = d[i][j] or (d[i][k] and d[k][j])
                    d[i][j]=d[i][k]+d[k][j]
                    p[i][j]=p[k][j]
    for i in range(n):
        if d[i][i]<0:
            circuit=1
            nod_circ=i
            return

INF = 99999
w=d=[ [0, 1, INF, INF],
          [INF, 0, -1, INF],
          [INF, INF, 0, -1],
          [INF, -1, INF, 0]]
#w matricea costurilor
#d matricea distantelor

#p[i][j] la pasul k = predecesorul lui j pe drumul minim curent
    # gasit de la i la j care are varfurile intermediare {1,2..,k}
#declarare p
p=[[0, 0, 0, 0], #p matrice predecesori
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
         ]
n = 4
circuit=0
nod_circ=None
floydWarshall()
if circuit==1:
    print("Avem circuit negativ:", end=" ")

    init=nod_circ
    while p[init][nod_circ]!=init:
        print(nod_circ, end=" ")
        nod_circ=p[init][nod_circ]
    print(nod_circ)


else:
    print("Matricea distantelor: ", d)

'''
    punctul B
    -> extrenticitatea d max de la u la restul varfurilor
    -> raza extrenticitatea minima a tuturor varfurilor = min(max)
    -> centrul = vf care au extrenticitatea minima
    -> extrenticitatea maxima max(max) =diametru= cea mai mare distanta intre doua varfuri 
'''