n=int(input())
for i in range(n):
    m=list(input())
    k=list(m)
    k=k[::-1]
    if m==k and len(m)%2==0:
        print("YES", "EVEN")
    elif m==k and len(m)%2!=0:
        print("YES", "ODD")
    else:
        print("NO")
        
        