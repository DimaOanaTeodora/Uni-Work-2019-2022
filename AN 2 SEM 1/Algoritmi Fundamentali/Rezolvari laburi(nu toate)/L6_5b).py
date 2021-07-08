'''
    se da un graf ORIENTAT
    vrea sa verfici daca are un drum eulerian
    conditii:
    d-(v)=d+(v)
    d-(x)=d+(x)-1 && d-(y)=d+(y)-1 && pt orice v\{x,y} d-(v)=d+(v)
    (grad intern -, grad extern +)
'''
n=5
#lucrez de la 0 ca sa mi fie mai usor
graf=[[0,1], [1,2], [2,1], [1,4], [4,0], [2,4], [3,2], [4,3]]
#calculez gradele interne si externe pt fiecare nod
grade={}
for i in range(n):
    grade[i]=[0,0] #-/+
for l in graf:
    grade[l[0]][1]+=1 #iese din l[0] +
    grade[l[1]][0]+=1 #intra in l[1] -
#verific existenta drum
ok=1
for i in range(n):
    if grade[i][0]!=grade[i][1]:
        ok=0
        break
if ok==1:
    print("are drum eulerian")
    #ma folosesc de algoritmul de ciclu
