n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=[]
for i in range(0,len(l)):
    if l[i]==m:
        c.append(i)
if len(c)>0:
    print(*c)
else:
    print(-1)
