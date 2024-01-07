a=int(input())
l=list(map(int,input().split()))
b=0
for  i in range(len(l)):
     if l[i]%2==0:
         b=i
print(b)