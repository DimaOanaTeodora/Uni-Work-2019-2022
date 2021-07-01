b=[1,5,10,50,100,200,500]
s=121
b=sorted(b,reverse=True)

i=0
sol=[]
while s>0:
    if b[i]<=s:
       sol.append((b[i],s//b[i]))
       s%=b[i]
    i+=1
print(sol)
