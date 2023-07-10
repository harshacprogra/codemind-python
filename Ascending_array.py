n=int(input())
l=list(map(int,input().split()))
a=1
d=0
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
        d=1
    else:
        a=0
if d==1 and a==1:
    print("yes")
else:
    print("no")
    