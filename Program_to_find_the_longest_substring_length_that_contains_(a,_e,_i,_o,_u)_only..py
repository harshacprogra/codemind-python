s=input()#abeeec
l=[]
c=0
v="aeiouAEIOU"#vowels
for i in s:
    if i in v:
        c+=1
    else:
        c=0
    l.append(c)
print(max(l))