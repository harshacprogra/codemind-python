n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    v=str(i)
    k=len(v)
    p.append(k)
    o=max(p)
print(p.count(o))