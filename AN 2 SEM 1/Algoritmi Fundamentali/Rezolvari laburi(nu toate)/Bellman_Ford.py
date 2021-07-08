'''
    Arcele pot avea si cost negativ
    graful nu contine circuite de cost negativ
    DETECTEAZA CIRCUITELE neafisand solutia optima
    Toate varfurile trebuie sa fie accesibile din nodul de start
    O(nm)
'''
n=5
muchii=[
    (1,4,1), (4,2,-1), (2,3,-1), (5,4,-6), (2,5,5)

]
#initializari
s=1
start=s
dist = [float("Inf")] * (n+1)
dist[start] = 0
tata=[0]*(n+1)
circuit=0
for i in range(1,n):
    for m in muchii:
        if dist[m[0]] != float("Inf") and dist[m[0]] +m[2] < dist[m[1]]:
            dist[m[1]]=dist[m[0]] + m[2]
            tata[m[1]]=m[0]
print(tata)
print(dist)
dist=[0,0,-8,-9,-7,-3]
#cod in plus pt detectare circuite
for m in muchii:
    if dist[m[0]]!= float("Inf") and dist[m[0]] + m[2] < dist[m[1]]:
        print("du, w(u,v) dv u v",  dist[m[0]] , m[2], dist[m[1]], m[0], m[1])
        dist[m[1]] = dist[m[0]] + m[2]
        tata[m[1]] = m[0]
        circuit=1
        nod_ac=m[0]
        break #exista circuit negativ

if circuit==1:
    print("circuit negativ")
    print("circuitul este:", end=" ")
    copie=nod_ac
    print(copie, end=" ")
    while tata[nod_ac]!=copie:
        print(tata[nod_ac], end=" ")
        nod_ac=tata[nod_ac]
    print(copie)
else:
    print("graful nu contine circuite de cost negativ")
    print("Vectorul de distante este: ",dist[1:])
    print("Vectorul de tati este: ", tata[1:])
    #acolo unde distanta este infinit inseamna ca nu e accesibil
    for i in range(1, n+1):
        if dist[i]!=float("Inf"):
            ss=i
            print("drum de la s la", i,":", end=" ")
            while tata[ss]!=0:
                print(ss, end=" ")
                ss=tata[ss]
            print(s)
            #ai grija ca le pune invers
        else:
            print("nodul", i, "nu e accesibil din s")