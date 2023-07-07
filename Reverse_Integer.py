k=int(input())
if k<0:
    k=-k
    m=str(k)
    l=list(m)
    l.reverse()
    o=''.join(l)
    o=int(o)
    print(-o)
else:
    m=str(k)
    l=list(m)
    l.reverse()
    o=''.join(l)
    o=int(o)
    print(o)
    