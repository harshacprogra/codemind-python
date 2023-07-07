n=int(input())
fib=[0,1]
while fib[-1] < n:
    fib.append(fib[-1]+fib[-2])
if n in fib:
    print(n)
elif fib[-1]-n<n-fib[-2]:
    print(fib[-1])
elif fib[-1]-n>n-fib[-2]:
    print(fib[-2])
else:
    print(fib[-2],fib[-1])

    
    
        