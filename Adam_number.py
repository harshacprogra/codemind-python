n = int(input())
num_square = n ** 2
reverse_num = int(str(n)[::-1])
reverse_square = reverse_num ** 2
if num_square == int(str(reverse_square)[::-1]):
    print(True)
else:
    print(False)
    