n=int(input())
l=list(map(int,input().split()))
h=list(l)
h.sort(reverse=True)
if l==h:
    print("yes")
else:
    print("no")