v=int(input())#128
w=int(input())
for i in range(v,w+1):
    j=str(i)
    c=0
    if "0" not in j:
        for k in range(len(j)):
            if j[k]!=0:
                if i%int(j[k])==0:
                    c+=1
    if c==len(j):
        print(j,end=" ")