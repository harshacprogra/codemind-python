n=int(input())
fib=[0,1]
while fib[-1]<n:
    fib.append(fib[-1]+fib[-2])
if n in fib:
    print(n)
