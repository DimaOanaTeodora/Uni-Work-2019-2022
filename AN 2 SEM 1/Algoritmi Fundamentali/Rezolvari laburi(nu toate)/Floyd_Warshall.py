'''
    ->matricea costurilor
    =>matricea distantelor rezultat
    =>matricea de predecesori la un anumit pas k
    O(n^3)
    merge si pe costuri negative
    dar graful sa nu aiba circuite negative
    CA SA-MI FIE MAI USOR PLEC CU NODURILE DE LA 0
'''
def floydWarshall():
    global w,d, n,p, INF
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

INF = 99999
w=d = [[0, 5, 10, 1], #w matricea costurilor
         [INF, 0, 3, INF],  #d matricea distantelor
         [INF, INF, 0, 2],
         [3, 20, 16, 0]
         ]
#p[i][j] la pasul k = predecesorul lui j pe drumul minim curent
    # gasit de la i la j care are varfurile intermediare {1,2..,k}
#pot sa fac doar DECLARARE AICI
p=[[0, 1, 1, 1], #p matrice predecesori
    [0, 0, 2, 0],
    [0, 0, 0, 3],
    [4, 4, 4, 0]
         ]
n = 4
floydWarshall()
print("Matricea drumurilor minime: ", d)
print("Matrice de predecesori: ", p)