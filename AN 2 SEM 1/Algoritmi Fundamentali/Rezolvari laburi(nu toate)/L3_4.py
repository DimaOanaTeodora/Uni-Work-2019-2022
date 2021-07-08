'''
    Conectarea cu cost minim a nodurilor la mai multe surse
    O(E log (M+N))
'''
import math
def dist(a,b):
    return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])
n=2 #nr centrale
m=5 #nr blocuri
centrale=[(0,0), (0,4)]
blocuri=[(1,4), (1,3), (1,1), (1,0), (3,0)]
best=[-1]*m
sel=[0]*m
sol=0
conect=[(1,2), (2,3), (3,4), (4,5), (5,6), (1,6), (3,5), (5,7), (6,7)]
for i in range (n):
    for j in range(m):
        val=dist(centrale[i], blocuri[j])
        if val<best[j] or best[j]==-1:
            best[j]=val

for j in range(m):
    ind=-1
    for i in range(m):
        if sel[i]:
            continue
        if ind==-1:
            ind=i
            continue
        if best[ind]>best[i]:
            ind=i
    sol=sol+math.sqrt(best[ind])
    sel[ind]=1
    for i in range(m):
        if sel[i]:
            continue
        val=dist(blocuri[ind], blocuri[i])
        best[i]=min(best[i], val)

print(sol)
print(best)





