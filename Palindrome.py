n=int(input())
k=str(n)
l=list(k)
l=l[::-1]
x=''.join(l)
if k==x:
    print(True)
else:
    print(False)