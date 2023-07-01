for i in range(int(input())):
    s=input().split()
    s1=[""]
    for i in s[0]:
        if s1[-1]!=i:
            s1.append(i)
    print((len(s[0])-len(s1))+1)