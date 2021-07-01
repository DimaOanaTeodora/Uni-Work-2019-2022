a=[(2,'a'),(4,'v'),(3,'v'),(1,'r'), ]
a=sorted(a,reverse=True, key=lambda x: x[0])

T=[]
T.append(a[0])
k=0


for i in range(len(a)):
    if T[k][1]!=a[i][1]:
        T.append(a[i])
        k+=1


print(T)


