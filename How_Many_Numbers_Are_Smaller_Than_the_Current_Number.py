n=int(input())#5
l=list(map(int,input().split()))
m=l
c=[]
for i in l:
    s=0
    for j in range(0,len(m)):
        if i>m[j]:
            s+=1
    c.append(s)
print(*c)

    
    
    
    
    
    