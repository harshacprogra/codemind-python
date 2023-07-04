n=int(input())
l=list(map(int,input().split()))
m=int(input())
x=max(l)#5
c=[]
for i in range(0,len(l)):
    if l[i]+m>=x:
        c.append(True)
    else:
        c.append(False)
print(*c)        
