n=int(input())
k=str(n)
l=list(k)
x=set(l)
if len(l)==len(x):
    print("Unique Number")
else:
    print("Not Unique Number" )