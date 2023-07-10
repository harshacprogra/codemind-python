n=int(input())
while True:
    ha=0
    s=str(n)
    for i in s:
        ha+=int(i)**2
    n=ha
    if n<=9:
        break
if n==7 or n==1:
    print(True)
else:
    print(False)
