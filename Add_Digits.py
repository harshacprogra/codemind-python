a=int(input())
x=True
while x:
    a=str(a)
    a=list(a)
    a=[eval(i) for i in a]
    if len(a)==1:
        print(a[0])
        break
    sm=sum(a)
    a=sm


