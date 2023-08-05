m=input()
k="aeiou"
c=0
d=0
for i in m:
    if i in k and c==0:
        print("V",end="")
        c=1
        d=0
    elif  i not in k and d==0:
        print("C",end="")
        c=0
        d=1
        
            
        
