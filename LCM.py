l,m=map(int,input().split())
for i in range(1,l*m):
    s1=l*i
    for j in range(1,l*m):
        s2=m*j
        if s1==s2:
            print(s1)
            break
    if s1==s2:
        break
    
    