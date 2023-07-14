s=input()
v="aeiou"
m=[]
for i in range(0,len(s)):
    for j in range(i,len(s)):
        c=0
        for k in s[i:j+1]:
            if k in v:
                c+=1
        if c==len(s[i:j+1]):
            m.append(c)
print(max(m))