num = int(input())
a, b = 0, 1
while b < num:
    a, b = b, a + b

if b == num:
    print(True)
else:
    print(False)