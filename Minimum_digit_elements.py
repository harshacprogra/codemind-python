n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    v=str(i)
    m=len(v)
    p.append(m)
    o=min(p)
print(p.count(o))

