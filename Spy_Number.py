n=input()
sum_1=0
product=1
for i in n:
    sum_1=sum_1+int(i)
    product=product*int(i)
if sum_1==product:
    print("Spy Number")
else:
    print("Not Spy Number")
    