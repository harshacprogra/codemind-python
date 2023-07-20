import itertools as it
s=input()
l=it.groupby(s)
k=[]
for i,v in l:
    k.append(len(list(v)))
print(max(k))